from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (assuming you have the appropriate driver installed)
driver = webdriver.Chrome()

try:
    # Set a page load timeout
    driver.set_page_load_timeout(30)  # Set timeout to 30 seconds

    # Open the webpage
    driver.get("https://finance.yahoo.com/")

    # Wait for the search input field to appear (you can use any other element)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "yfin-usr-qry")))

    # Perform your automation actions here
    # For example, you can search for a stock symbol
    search_input = driver.find_element_by_id("yfin-usr-qry")
    search_input.send_keys("AAPL")
    search_input.submit()

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the WebDriver
    driver.quit()
