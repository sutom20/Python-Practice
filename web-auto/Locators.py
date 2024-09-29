from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# try:
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/angularpractice/')
print(driver.title)
print(driver.current_url)

driver.find_element(By.NAME, 'email').send_keys('abc@gmail.com')
print('email entered')

driver.find_element(By.NAME, 'name').send_keys('tomharry')
print('name entered')

driver.find_element(By.ID, 'exampleInputPassword1').send_keys('myPassword')
print('passowrd entered')

driver.find_element(By.ID, 'exampleCheck1').click()
print('checkbox clicked')

dropdown_element = driver.find_element(By.ID, 'exampleFormControlSelect1')
# dropdown_element.click()
print('dropdown clicked')
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text('Female')
time.sleep(5)
dropdown.select_by_index(0)
time.sleep(5)
# dropdown_element.click()

driver.execute_script("window.scrollTo(0, 0);")


driver.find_element(By.ID, 'inlineRadio2').click()
print('radio clicked')

# driver.find_element(By.XPATH, '//input[@id="dateofBirth"]').click()
# print('dob selector clicked')

driver.find_element(By.CSS_SELECTOR,"input[value = 'Submit']").click()

success_message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(success_message)

assert 'Success' in success_message



# except Exception as e:
#     print(e)
#
# finally:
#     time.sleep(5)

driver.quit()
