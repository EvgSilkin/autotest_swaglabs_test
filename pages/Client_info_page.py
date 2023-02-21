import allure

from base.Base import Base
from utilities.Logger import Logger

class Client_info_page(Base):

    def __init__(self, driver):
        super().__init__(driver);
        self.driver = driver;

    #Locators
    input_first_name = "//input[@id='first-name']"
    input_last_name = "//input[@id='last-name']"
    input_zip_postal_code = "//input[@id='postal-code']"
    button_continue = "//input[@id='continue']"
    finish_step_marker = "//span[@class='title']"


    #Getters
    def get_input_first_name(self):
        return self.get_element_to_be_clickable_by_xpath(self.input_first_name)
    def get_input_last_name(self):
        return self.get_element_to_be_clickable_by_xpath(self.input_last_name)
    def get_input_zip_postal_code(self):
        return self.get_element_to_be_clickable_by_xpath(self.input_zip_postal_code)
    def get_button_continue(self):
        return self.get_element_to_be_clickable_by_xpath(self.button_continue)
    def get_finish_step_marker_text(self):
        marker = self.get_visibility_of_element_located_by_xpath(self.finish_step_marker)
        return marker.text

    #Actions
    def click_button_continue(self):
        self.get_button_continue().click()


    #Methods
    def fill_client_form_and_continue(self, first_name, last_name, zip_postal_code):
        with allure.step("Fill client form and continue"):
            Logger.add_start_step(method="Fill client form and continue")
            self.get_input_first_name().send_keys(first_name)
            self.get_input_last_name().send_keys(last_name)
            self.get_input_zip_postal_code().send_keys(zip_postal_code)
            self.click_button_continue()
            self.assert_element_text('CHECKOUT: OVERVIEW', self.get_finish_step_marker_text())
            Logger.add_end_step(url=self.get_current_url(), method="Fill client form and continue")



