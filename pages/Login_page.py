import allure

from base.Base import Base
from utilities.Logger import Logger

class Login_page(Base):

    def __init__(self, driver):
        super().__init__(driver);
        self.driver = driver;

    url = "https://www.saucedemo.com/"

    #Locators
    input_username = "//input[@id='user-name']";
    input_password = "//input[@id='password']";
    login_button = "//input[@id='login-button']";
    authorization_marker = "//span[@class='title']";

    #Getters
    def get_input_username(self):
        return self.get_element_to_be_clickable_by_xpath(self.input_username)

    def get_input_password(self):
        return self.get_element_to_be_clickable_by_xpath(self.input_password)

    def get_login_button(self):
        return self.get_element_to_be_clickable_by_xpath(self.login_button)

    def get_authorization_marker_text(self):
        marker = self.get_visibility_of_element_located_by_xpath(self.authorization_marker)
        return marker.text

    #Actions
    def fill_input_username(self, username):
        self.get_input_username().send_keys(username);

    def fill_input_password(self, password):
        self.get_input_password().send_keys(password);

    def click_login_button(self):
        self.get_login_button().click();

    #Methods
    def authorization(self, username, password):
        with allure.step("Authorization"):
            Logger.add_start_step(method="Authorization")
            print("\nStart authorization...")
            self.driver.get(self.url)
            self.driver.maximize_window()
            print("Current url: " + self.get_current_url())
            self.fill_input_username(username)
            self.fill_input_password(password)
            self.click_login_button()
            self.assert_element_text('PRODUCTS', self.get_authorization_marker_text())
            print("Authorization success:"
                  "\n\tLogin: " + username +
                  "\n\tPassword: " + password)
            Logger.add_end_step(url=self.get_current_url(), method="Authorization")

