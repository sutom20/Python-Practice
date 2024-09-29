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

driver.get('https://the-internet.herokuapp.com/windows')
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.LINK_TEXT, 'Click Here').click()

window_list = driver.window_handles
# print(window_list[1])
driver.switch_to.window(window_list[1])
print(driver.find_element(By.TAG_NAME, 'h3').text)
driver.close()
driver.switch_to.window(window_list[0])
parent_window = driver.find_element(By.TAG_NAME, 'h3').text

assert 'Opening' in parent_window

driver.quit()
