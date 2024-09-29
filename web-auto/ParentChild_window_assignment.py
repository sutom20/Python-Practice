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

driver.get('https://rahulshettyacademy.com/loginpagePractise/')
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.TAG_NAME, 'a').click()
windowsList = driver.window_handles

driver.switch_to.window(windowsList[1])
email = driver.find_element(By.XPATH, '//a[text()="mentor@rahulshettyacademy.com"]').text

driver.switch_to.window(windowsList[0])
driver.find_element(By.ID, 'username').send_keys(email)
driver.find_element(By.ID, 'password').send_keys('learning')
driver.find_element(By.ID, 'terms').click()
driver.find_element(By.ID, 'signInBtn').click()

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="alert alert-danger col-md-12"]')))

failure_message = driver.find_element(By.XPATH, '//div[@class="alert alert-danger col-md-12"]').text
print(failure_message)

time.sleep(3)
driver.quit()
