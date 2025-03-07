from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
import time

USR = "ypur_mail"
PASS = "your_password"

try:
    # Set up Chrome options to ignore certificate errors and run headless
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--headless')  # run in headless mode
    chrome_options.add_argument('--disable-gpu')  # recommended for headless
    chrome_options.accept_insecure_certs = True

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://172.16.16.250:8090/httpclient.html")
    time.sleep(1)

    try:
        # Locate elements
        username = driver.find_element(by=By.NAME, value="username")
        password = driver.find_element(by=By.NAME, value="password")
        btn = driver.find_element(by=By.ID, value="loginbutton")
    except NoSuchElementException as e:
        print("Error: One or more elements were not found on the page:", e)
    else:
        # Input credentials and click the login button
        username.send_keys(USR)
        password.send_keys(PASS)
        # driver.save_screenshot("D:\python_project\scrapper\screenshot.png")
        btn.click()

except WebDriverException as e:
    print("WebDriver error occurred:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    # Ensure the driver is closed even if errors occur
    driver.quit()
