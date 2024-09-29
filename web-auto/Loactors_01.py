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

driver.get('https://www.rahulshettyacademy.com/client/')

driver.find_element(By.LINK_TEXT, 'Forgot password?').click()
driver.find_element(By.XPATH, "//form//div//input[@type = 'email']").send_keys('demo@gmail.com')
driver.find_element(By.XPATH, "//div//input[@type = 'password']").send_keys('Abc123')
driver.find_element(By.ID, 'confirmPassword').send_keys('Abc123')
driver.find_element(By.XPATH, "//div//button[@type = 'submit']").click()


time.sleep(5)
driver.quit()
