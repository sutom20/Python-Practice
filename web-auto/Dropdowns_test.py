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

driver.get('https://rahulshettyacademy.com/angularpractice/')

# Static dropdown
dropdown_element = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
dropdown_element.select_by_visible_text('Female')
dropdown_element.select_by_index(0)

time.sleep(2)

driver.get('https://rahulshettyacademy.com/loginpagePractise/')
static_1 = Select(driver.find_element(By.XPATH, '//select[@class="form-control"]'))
static_1.select_by_value('teach')

time.sleep(2)


driver.close()
