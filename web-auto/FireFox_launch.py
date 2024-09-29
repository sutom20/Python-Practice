from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service_obj = Service()
driver = webdriver.Edge\
    (Service == service_obj)
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/')
print(driver.title)
print(driver.current_url)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
# driver.minimize_window()
time.sleep(3)
driver.back()
time.sleep(3)

driver.refresh()
time.sleep(3)
 
driver.forward()
time.sleep(3)

driver.close()
