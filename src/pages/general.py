

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def is_displayed(self, locator):
        try:
            return self.find(locator).is_displayed()
        except:
            return False

    def get_text(self, locator):
        return self.find(locator).text

    def wait_until_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def get_title(self):
        return self.driver.title

