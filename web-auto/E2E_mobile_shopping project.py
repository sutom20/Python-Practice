import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# user_input = input('Please enter the mobile name you wish to buy ')
# user_input1 = input(("Please enter the Country for delivery location "))

user_input = 'iphone X'
user_input1 = 'India'

options = Options()
options.add_experimental_option("detach", True)

executables = ChromeDriverManager().install()
driver_service = Service(executables)

driver = webdriver.Chrome(service=driver_service, options=options)

driver.implicitly_wait(5)

driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()

driver.find_element(By.XPATH, "//a[contains(@href, 'shop')]").click()

# driver.find_element(By.XPATH, "//div//*[contains(text(), 'Samsung Note 8')]/following::*[4]").click()

add_buttons = driver.find_elements(By.XPATH, "//div[@class='card-footer']/button")
print(len(add_buttons))

mobile_names = driver.find_elements(By.XPATH, "//div[@class='card h-100']//h4/a")
print(len(mobile_names))

mobile_name_path = "//div[@class='card h-100']//h4/a[contains(text(), '"+user_input+"')]"
new_path = mobile_name_path + '/following::*[4]'

print(new_path)
# for i in mobile_names:
#     if i.get_attribute("text") == 'Samsung Note 8':
driver.find_element(By.XPATH, new_path).click()

driver.execute_script("window.scrollTo(0,0);")

# driver.find_element(By.XPATH, "//div[@class='container']//button[@aria-label='Toggle navigation']").click()
driver.find_element(By.XPATH, "//div[@class='container']//a[@class='nav-link btn btn-primary']").click()

mobile_added = driver.find_element(By.XPATH, "//div//h4[@class='media-heading']/a").get_attribute("text")
print(mobile_added)

assert mobile_added == user_input

driver.find_element(By.XPATH, "//button[contains(text(), 'Checkout')]").click()

driver.find_element(By.ID, 'country').send_keys(user_input1)
driver.find_element(By.XPATH, "//div[@class='suggestions']//a[contains(text(), user_input1)]").click()

wait = WebDriverWait(driver, 5)
wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'checkbox')]//label")))

driver.find_element(By.XPATH, "//div[contains(@class, 'checkbox')]//label").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

success_message = driver.find_element(By.XPATH, "//div[contains(@class, 'alert')]/strong").text
print(success_message)

assert "Success" in success_message

driver.find_element(By.XPATH, "//div[contains(@class, 'alert')]/a").click()
driver.quit()


