import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
options = Options()
options.add_experimental_option("detach", True)

service_ChromeDriver = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service_ChromeDriver, options = options)

driver.get('https://the-internet.herokuapp.com/iframe')
driver.maximize_window()
driver.implicitly_wait(5)

driver.switch_to.frame(driver.find_element(By.ID, 'mce_0_ifr'))
driver.find_element(By.ID, 'tinymce').clear()
driver.find_element(By.ID, 'tinymce').send_keys('input my content in iFrame')

driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, 'h3').text)

time.sleep(3)
driver.quit()
