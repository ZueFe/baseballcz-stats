"""
Scraping data from page `baseball.cz <http://baseball.cz>`_. Uses `Selenium <http://selenium-python.readthedocs.io/>`_
in combination with Firefox, or Chrome webdriver to save data locally. These can be then sent to FTP server as desired.
"""

from selenium import webdriver
import os
import constants as cs
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import Select
import time
import ftplib

def setup_chrome_opt():
    """
    Sets up options for Chrome webdriver. Based on defined `constants <constants.html>`_ it chooses where
    to save data and where Chrome binary and Chrome driver can be found.
    Sets following options:

    * *download.default_directory: constants.saveDir*
    * *download.prompt_for_download: False*
    * *download.directory_upgrade: True*
    * *safebrowsing.enaled: True*

    :returns: Set Chrome webdriver object
    """
    chrome_options = ChromeOptions()
    chrome_options.binary_location = cs.GOOGLE_CHROME_BIN
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    prefs = {'download.default_directory' : cs.saveDir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True}
    chrome_options.add_experimental_option('prefs', prefs)
    #chrome_options.add_argument('headless')
    driver = webdriver.Chrome(executable_path=cs.CHROMEDRIVER_PATH,chrome_options=chrome_options)


    return driver

def setup_firefox_opt():

    """
    Sets up options for Firefox webdriver. Based on defined `constants <constants.html>`_ it chooses where to save data.
    Sets following options:

    * *--headless*
    * *browser.download.folderList:2*
    * *browser.download.manager.showWhenStarting: False*
    * *browser.download.dir: constants.saveDir*
    * *browser.helperApps.neverAsk.saveToDisk: application/csv,text/csv,application/force-download*

    :returns: Set Firefox webdriver object
    """
    options = Options()
    options.add_argument('--headless')
    options.set_preference("browser.download.folderList",2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.dir", get_saveDir())
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/csv,text/csv,application/force-download")
    driver = webdriver.Firefox(firefox_options=options)

    return driver

def download_stats(category = cs.CATEGORIES[0], team_stats = False, browser='firefox'):
    """
    Locally saves statistics csv from `baseball.cz <http://baseball.cz>`_ based on the given category.
    File is stored in save directory defined in `constants <contants.html>_` script.
    Default values are for *individual batter*, using Firefox.

    :param category: Category of the statistics. Categories are defined  in `constants <constants.html>`_.
    :param team_stats: *(bool)* Whether the team or individual stats should be downloaded.
    :param browser: 'firefox' to use Firefox webdriver, otherwise Chrome webdriver will be used.
    """
    if browser == 'firefox':
        driver = setup_firefox_opt()
    else:
        driver = setup_chrome_opt()

    try:
        driver.get('https://www.baseball.cz/modules.php?op=modload&name=liga&file=index&do=statx&akce=432&pda=2&admina=')

        cat = Select(driver.find_element_by_name('xco'))
        cat.select_by_value(category)

        typ = Select(driver.find_element_by_name('xtyp'))
        typ.select_by_index(cs.TYPES["týmový"] if team_stats else cs.TYPES['individuální'])

        elem = driver.find_elements_by_xpath("//*[contains(text(), 'Exportovat')]")[0]
        elem.click()

        #Wait for the download 0.8 minutes
        time.sleep(0.8)

        #TODO: better naming conventions for team/individual
        downloaded_file = os.path.join(get_saveDir(), "stats.csv")
        new_filename = "stats_{}_{}.csv".format(category, 'team' if team_stats else 'individual')
        new_filepath = os.path.join(get_saveDir(), new_filename)
        os.replace(downloaded_file, new_filepath)
    finally:
        driver.close()

def get_saveDir():
    """
    Return save directory defined in `constants <constants.html>`_.
    :returns: String containing path to save directory.
    """
    return cs.saveDir

def cleanup_dir():
    """
    Removes all data in save directory defined in `constants <constants.html>`_.
    """
    files = os.listdir(get_saveDir())

    for f in files:
        os.remove('{}{}'.format(get_saveDir(),f))

def download_team_stats():
    """
    Downloads all team statistics and saves them to the save directory defined in `constants <constants.html>`_.
    """
    #TODO improve
    print("Started downloading team stats.")
    for cat in cs.CATEGORIES:
        download_stats(cat, team_stats = True)

    print("Done.")

def download_single_stats():
    """
    Downloads all individual statistics and saves them to the save director defined in `constants <constants.html>`_.
    """
    #TODO improve
    print("Started downloading single stats.")
    for cat in cs.CATEGORIES:
        download_stats(cat)

    print("Done.")

def download_all():
    """
    Downloads all individual and team statistics and saves them to the save directory defined in `constants <constants.html>`_.
    """
    download_team_stats()
    download_single_stats()

def send_to_ftp():
    """
    Allows to send all files from directory *./data/* to FTP server. Due to its use on a server and security
    reasons, information about the FTP server are set as enviromental variables.

    Enviromental variables:

        * FTP_SERVER -- http to FTP host
        * FTP_PORT -- number of the opened FTP port
        * FTP_NAME -- login name to FTP server
        * FTP_PASSWRD -- login password to FTP server
        * FTP_PATH -- path on FTP server where files should be sent to
    """
    ftp = ftplib.FTP()
    ftp.connect(os.environ['FTP_SERVER'], int(os.environ['FTP_PORT'])) #host, port
    ftp.login(os.environ['FTP_NAME'], os.environ['FTP_PASSWRD'])
    ftp.cwd(os.environ['FTP_PATH'])

    files = os.listdir('data')
    for f in files:
        opened = open(os.path.join('data',f), 'rb')
        print(opened)
        ftp.storbinary('STOR {}'.format(f), opened)
        opened.close()

    ftp.close()
