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
# options.add_argument("headless")
options.add_argument('--ignore-certificate-errors')

service_ChromeDriver = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service_ChromeDriver, options = options)

actions = ActionChains(driver)

driver.get('https://www.flipkart.com/')
driver.maximize_window()
driver.implicitly_wait(5)
# import pandas as pd
#
#
#
# data = {'Name': ['John', 'Sunny', 'Koel', 'Veer', 'Shubham'],
#         'Age': [30, 28, 19, 27, 30],
#         'Courses': ['Python', 'Java', 'Java', 'C', 'Go']}
#
# df = pd.DataFrame.from_dict(data)
# df.head(15)
#
# df.columns
#
#
# df[(df['Age']) < 28]
#
# list_1 = [3, 6, 4 , 6, 8 , 9]
#
# lambda_func = lambda x : sum(x)
# lambda_func(list_1)
#
# sq_list_1 = [x*x for x in list_1]


item_categories = driver.find_elements(By.CSS_SELECTOR, "._1XjE3T")

# //div[@class='_16rZTH']//a

for item in item_categories:
        print(item.text)
        if item.text == 'Electronics':
              item.click()

time.sleep(5)

sub_categories = driver.find_elements(By.XPATH, "//div[@class='_16rZTH']//a/@href")

for sub_cat in sub_categories:
        print(sub_cat.text)
        # if 'Computer' in sub_cat.text:
        #         sub_cat.click()
        # break


driver.quit()

