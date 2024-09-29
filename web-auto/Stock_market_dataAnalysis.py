import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.implicitly_wait(5)

driver.get("https://finance.yahoo.com/")
driver.maximize_window()
driver.find_element(By.ID, 'yfin-usr-qry').send_keys('Nifty 50')

driver.find_element(By.ID, 'header-desktop-search-button').click()

driver.quit()

