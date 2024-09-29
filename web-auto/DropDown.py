from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


service_obj = Service(ChromeDriverManager().install())
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service_obj, options=options)

driver.get('https://www.rahulshettyacademy.com/dropdownsPractise/')

driver.find_element(By.ID, 'autosuggest').send_keys('ind')
time.sleep(2)

# store the list of countries
countries = driver.find_elements(By.XPATH, "//li[@class = 'ui-menu-item']//a")
print(len(countries))

for country in countries:
    if country.text == 'India':
        country.click()
        break

assert driver.find_element(By.ID, 'autosuggest').get_attribute('value') == 'India'

time.sleep(2)


driver.quit()
