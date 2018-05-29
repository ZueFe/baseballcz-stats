import os
import download as dw
import constants as cs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

chrome_options = Options()
chrome_options.binary_location = cs.GOOGLE_CHROME_BIN
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
prefs = {"download.default_directory" : cs.saveDir, "directory_upgrade": True, 'download.prompt_for_download': False,}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path=cs.CHROMEDRIVER_PATH, chrome_options=chrome_options)

driver.get('https://www.baseball.cz/modules.php?op=modload&name=liga&file=index&do=statx&akce=432&pda=2&admina=')

cat = Select(driver.find_element_by_name('xco'))
cat.select_by_value(cs.CATEGORIES[0])

typ = Select(driver.find_element_by_name('xtyp'))
typ.select_by_index(cs.TYPES['individuální'])

elem = driver.find_elements_by_xpath("//*[contains(text(), 'Exportovat')]")[0]
elem.click()

#dw.download_stats()
print(os.listdir(os.path.join('.', "data")))
