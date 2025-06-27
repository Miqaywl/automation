from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import chromedriver as ch


# service = webdriver.Chrome()


driver = webdriver.Chrome()


driver.get("https://practicetestautomation.com/practice-test-login/")



WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "username"))
).send_keys("student")


driver.find_element(By.ID, "password").send_keys("Password123")


driver.find_element(By.ID, "submit").click()



input()
driver.quit()
