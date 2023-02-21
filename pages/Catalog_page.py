import allure

from base.Base import Base
from utilities.Logger import Logger

class Catalog_page(Base):

    def __init__(self, driver):
        super().__init__(driver);
        self.driver = driver;

    #Locators
    button_add_to_cart_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    button_add_to_cart_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    price_of_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']/preceding-sibling::div[@class='inventory_item_price']"
    price_of_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']/preceding-sibling::div[@class='inventory_item_price']"
    link_to_cart = "//a[@class='shopping_cart_link']"
    cart_marker = "//span[@class='title']"

    #Getters
    def get_button_add_to_cart_product_1(self):
        return self.get_element_to_be_clickable_by_xpath(self.button_add_to_cart_product_1)
    def get_button_add_to_cart_product_2(self):
        return self.get_element_to_be_clickable_by_xpath(self.button_add_to_cart_product_2)
    def get_price_of_product_1(self):
        return self.get_visibility_of_element_located_by_xpath(self.price_of_product_1)
    def get_price_of_product_2(self):
        return self.get_visibility_of_element_located_by_xpath(self.price_of_product_2)
    def get_link_to_cart(self):
        return self.get_visibility_of_element_located_by_xpath(self.link_to_cart)
    def get_cart_marker_text(self):
        marker = self.get_visibility_of_element_located_by_xpath(self.cart_marker)
        return marker.text

    #Actions
    def click_button_add_to_cart_product_1(self):
        self.get_button_add_to_cart_product_1().click()
    def click_button_add_to_cart_product_2(self):
        self.get_button_add_to_cart_product_2().click()
    def click_link_to_cart(self):
        self.get_link_to_cart().click()
    def return_float_price_of_product_1(self):
        return float(self.get_price_of_product_1().text.replace("$", ""))
    def return_float_price_of_product_2(self):
        return float(self.get_price_of_product_2().text.replace("$", ""))

    #Methods
    def add_to_cart_two_products_and_return_sum_price(self):
        with allure.step("Add to cart two products and return sum price"):
            Logger.add_start_step(method="Add to cart two products and return sum price")
            product_price_sum = self.return_float_price_of_product_1() + self.return_float_price_of_product_2()
            self.click_button_add_to_cart_product_1()
            self.click_button_add_to_cart_product_2()
            self.click_link_to_cart()
            Logger.add_end_step(url=self.get_current_url(), method="Add to cart two products and return sum price")
            return product_price_sum
    def follow_to_cart(self):
        with allure.step("Follow to cart"):
            Logger.add_start_step(method="Follow to cart")
            self.click_link_to_cart()
            self.assert_element_text('YOUR CART', self.get_cart_marker_text())
            Logger.add_end_step(url=self.get_current_url(), method="Follow to cart")

