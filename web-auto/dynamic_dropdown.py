import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

service_ChromeDriver = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service_ChromeDriver, options = options)

driver.get('https://rahulshettyacademy.com/dropdownsPractise/')

driver.find_element(By.ID, 'autosuggest').send_keys('Ind')

time.sleep(2)

country_list = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

print(country_list)

for country in country_list:
    if country.text == 'India':
        country.click()
        break

assert driver.find_element(By.ID, 'autosuggest').get_attribute("value") == 'India'

time.sleep(2)

driver.quit()
