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

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
name = 'Sumit'
driver.find_element(By.ID, 'name').send_keys(name)
driver.find_element(By.ID, 'alertbtn').click()
alert = driver.switch_to.alert

alert_text = alert.text
print(alert_text)

assert name in alert_text
alert.dismiss()

time.sleep(2)

driver.quit()
