import time
from selenium import webdriver
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
options.add_argument("--disable-gpu")

service_ChromeDriver = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service_ChromeDriver, options = options)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, '//a[text()="Top Deals"]').click()
window_list = driver.window_handles
driver.switch_to.window(window_list[1])

# sort using web
# driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

actual_list = []
web_table_elements = driver.find_elements(By.XPATH, '//table//tr//td[1]')
print(len(web_table_elements))

for i in web_table_elements:
    actual_list.append(i.text)
# apply sort on actual list and store as py_sorted_list
print(actual_list)

actual_list_copy = actual_list.copy()
actual_list.sort()

assert actual_list_copy == actual_list
# click on websort option and fetch the sorted list as web_sorted_list
# web_sorted_list = []
# post_sort_table_elements = driver.find_elements(By.XPATH, '//table//tr//td[1]')
#
# for i in post_sort_table_elements:
#     web_sorted_list.append(i.text)
#
# print(web_sorted_list)
# compare the py_sorted_list to web_sorted_list

time.sleep(3)
driver.quit()
