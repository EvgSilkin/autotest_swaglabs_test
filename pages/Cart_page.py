import allure

from base.Base import Base
from utilities.Logger import Logger

class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver);
        self.driver = driver;

    #Locators
    button_checkout = "//button[@id='checkout']"
    price_of_product_1 = "//button[@id='remove-sauce-labs-backpack']/preceding-sibling::div[@class='inventory_item_price']"
    price_of_product_2 = "//button[@id='remove-sauce-labs-bike-light']/preceding-sibling::div[@class='inventory_item_price']"
    client_info_marker = "//span[@class='title']"

    #Getters
    def get_button_checkout(self):
        return self.get_element_to_be_clickable_by_xpath(self.button_checkout)
    def get_price_of_product_1(self):
        return self.get_visibility_of_element_located_by_xpath(self.price_of_product_1)
    def get_price_of_product_2(self):
        return self.get_visibility_of_element_located_by_xpath(self.price_of_product_2)
    def get_client_info_marker_text(self):
        marker = self.get_visibility_of_element_located_by_xpath(self.client_info_marker)
        return marker.text

    #Actions
    def click_button_checkout(self):
        self.get_button_checkout().click()
    def return_float_price_of_product_1(self):
        return float(self.get_price_of_product_1().text.replace("$", ""))
    def return_float_price_of_product_2(self):
        return float(self.get_price_of_product_2().text.replace("$", ""))

    #Methods
    def get_sum_product(self):
        with allure.step("Get sum product"):
            Logger.add_start_step(method="Get sum product")
            product_price_sum = self.return_float_price_of_product_1() + self.return_float_price_of_product_2()
            Logger.add_end_step(url=self.get_current_url(), method="Get sum product")
        return product_price_sum

    def action_checkout(self):
        with allure.step("Action checkout"):
            Logger.add_start_step(method="Action checkout")
            self.click_button_checkout()
            self.assert_element_text('CHECKOUT: YOUR INFORMATION', self.get_client_info_marker_text())
            Logger.add_end_step(url=self.get_current_url(), method="Action checkout")

