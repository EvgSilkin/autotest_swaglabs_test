import allure

from base.Base import Base
from utilities.Logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Name_page(Base):

    def __init__(self, driver):
        super().__init__(driver);
        self.driver = driver;

    url = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    #Locators
    input_username = "//input[@id='user-name']";
    input_password = "//input[@id='password']";
    login_button = "//input[@id='login-button']";
    authorization_marker = "//span[@class='title']";

    #Getters
    def get_input_username(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_username)))

    def get_input_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.input_password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_authorization_marker_text(self):
        marker = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.authorization_marker)))
        return marker.text

    #Actions
    def fill_input_username(self):
        self.get_input_username().send_keys(self.username);

    def fill_input_password(self):
        self.get_input_password().send_keys(self.password);

    def click_login_button(self):
        self.get_login_button().click();

    #Methods
    def authorization(self):
        with allure.step("authorization"):
            Logger.add_start_step(method="authorization")
            print("\nStart authorization...")
            self.driver.get(self.url)
            print("Current url: " + self.get_current_url())
            self.fill_input_username()
            self.fill_input_password()
            self.click_login_button()
            self.assert_element_text('PRODUCTS', self.get_authorization_marker_text())
            print("Authorization success:"
                  "\n\tLogin: " + self.username +
                  "\n\tPassword: " + self.password)
            Logger.add_end_step(url=self.get_current_url(), method="authorization")