import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
options.add_argument('headless')
options.add_argument('--ignore-certificate-errors')

service_ChromeDriver = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service_ChromeDriver, options = options)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.get_screenshot_as_file('screen.png')

driver.quit()
