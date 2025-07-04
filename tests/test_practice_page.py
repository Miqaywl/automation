import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conf.conftest import driver
from src.locatores.selectors import LoginPage
from src.pages.general import BasePage


def test_practice_page(driver):
    page = BasePage(driver)
    page.open("https://practicetestautomation.com/practice/")

    page.click((By.CSS_SELECTOR,
                ".wp-block-column a[href*='practice-test-login']")
               )

    success_msg = page.find((By.TAG_NAME, "h2"))
    assert success_msg.text == "Test login"

    page.open("https://practicetestautomation.com/practice/")
    page.click((By.CSS_SELECTOR,
                ".wp-block-column a[href*='practice-test-exceptions']")
               )
    success_msg1 = page.find((By.TAG_NAME, "h2"))

    assert success_msg1.text == "Test Exceptions"