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

service_ChromeDriver = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service_ChromeDriver, options = options)

driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")

ber_prods = driver.find_elements(By.XPATH, "//div[@class='product']//button")
results = len(ber_prods)

assert results > 0

for prods in ber_prods:
    prods.click()

driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()
driver.find_element(By.XPATH, "//*[contains(text(), 'PROCEED')]").click()
driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.promoInfo' )))

promo = driver.find_element(By.CSS_SELECTOR, '.promoInfo').text
assert 'applied' in promo

total_amount = float(driver.find_element(By.CSS_SELECTOR, '.totAmt').text)
print(total_amount)

individual_price_list = driver.find_elements(By.XPATH, '//tr/td[5]/p')

print(individual_price_list)

sum = 0
for price in individual_price_list:
    sum = int(price.text) + sum

print(sum)

assert sum == total_amount

discounted_amt = float(driver.find_element(By.CSS_SELECTOR, '.discountAmt').text)
print(discounted_amt)

assert discounted_amt < total_amount

driver.find_element(By.XPATH, "//button[contains(text(), 'Place Order')]").click()

country_dropdown = Select(driver.find_element(By.XPATH,'//div//select'))
country_dropdown.select_by_visible_text('India')
user_country = country_dropdown.first_selected_option.text
print(user_country)
my_country = 'India'

assert user_country == my_country

terms_conditions = driver.find_element(By.XPATH, '//div//input[@type="checkbox"]')
terms_conditions.click()
assert terms_conditions.is_selected()

driver.find_element(By.XPATH, '//button[contains(text(), "Proceed")]').click()
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="wrapperTwo"]/span')))

success_message = 'your order has been placed successfully'

order_success = driver.find_element(By.XPATH, '//div[@class="wrapperTwo"]/span').text
print(order_success)

assert success_message in order_success

time.sleep(2)

driver.quit()
