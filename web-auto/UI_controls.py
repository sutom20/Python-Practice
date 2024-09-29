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

# select option 2 check box

checkbox_list = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for checkbox in checkbox_list:
    if checkbox.get_attribute("value") == 'option1':
        checkbox.click()
        assert checkbox.is_selected()
        break

radio_list = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(radio_list))

for radio in radio_list:
    if radio.get_attribute("value") == "radio2":
        radio.click()
        assert radio.is_selected()
        break

hidden_text = driver.find_element(By.ID, 'displayed-text')
assert hidden_text.is_displayed()
driver.find_element(By.ID, 'hide-textbox').click()
time.sleep(2)
assert not hidden_text.is_displayed()

time.sleep(2)

driver.quit()
