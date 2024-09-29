from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

executables = ChromeDriverManager().install()
service = Service(executables)

driver = webdriver.Chrome(service=service, options=options)

driver.get('https://books.toscrape.com/')
driver.maximize_window()

results = driver.find_elements(By.XPATH, "//article[p[@class='star-rating One']]//a | //article[p[@class='star-rating One']]//p[@class='price_color']")

for i in results:
    if i.tag_name == "a":
        print(i.get_attribute("title"))
    else:
        if i.tag_name == "p":
            print(i.get_attribute("innerHTML"))



driver.quit()
