

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conf.conftest import driver
from src.selectors import LoginPage




def test_successful_login(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, LoginPage.username))
    ).send_keys("student")

    driver.find_element(By.ID, LoginPage.password).send_keys("Password123")
    driver.find_element(By.ID, LoginPage.submit_button).click()


    success_msg = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    assert success_msg.text == "Logged In Successfully"
