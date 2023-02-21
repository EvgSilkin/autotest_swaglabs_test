import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait


class Base():

    def __init__(self, driver):
        self.driver = driver;

    def get_current_url(self):
        return self.driver.current_url

    def assert_element_text(self, text, result):
        assert text == result

    def assert_url(self, result):
        current_url = self.get_current_url()
        assert current_url == result

    def screen_page(self, path):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot(f"{path}" + f"{name_screenshot}")

    def get_element_to_be_clickable_by_xpath(self, locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, locator)))
    def get_visibility_of_element_located_by_xpath(self, locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))