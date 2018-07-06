from selenium import webdriver
import os
import local.constants as cs
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
import time


def setup_firefox_opt():
    options = Options();
    options.add_argument('--headless')
    options.set_preference("browser.download.folderList",2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.dir", get_saveDir())
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/csv,text/csv,application/force-download")
    driver = webdriver.Firefox(firefox_options=options)

    return driver

def download_stats(category = cs.CATEGORIES[0], team_stats = False):
    driver = setup_firefox_opt()

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
    if not os.path.isdir(cs.saveDir):
        os.mkdir(cs.saveDir)

    return cs.saveDir

def cleanup_dir():
    files = os.listdir(get_saveDir())

    for f in files:
        os.remove('{}{}'.format(get_saveDir(),f))

def download_team_stats():
    #TODO improve
    print("Started downloading team stats.")
    for cat in cs.CATEGORIES:
        download_stats(cat, team_stats = True)

    print("Done.")

def download_single_stats():
    #TODO improve
    print("Started downloading single stats.")
    for cat in cs.CATEGORIES:
        download_stats(cat)

    print("Done.")

def download_all():
    download_team_stats()
    download_single_stats()
