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
options.add_argument("headless")
options.add_argument('--ignore-certificate-errors')

service_ChromeDriver = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service_ChromeDriver, options = options)

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
driver.implicitly_wait(5)

actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.ID, 'mousehover')).perform()

# actions.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
actions.move_to_element(driver.find_element(By.ID, 'mousehover')).perform()

actions.move_to_element(driver.find_element(By.LINK_TEXT, 'Reload')).click().perform()
time.sleep(2)

actions.drag_and_drop(driver.find_element(By.ID, 'mousehover'),driver.find_element(By.ID, 'mousehover'))

driver.quit()
