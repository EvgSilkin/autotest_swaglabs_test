import allure


from base.Base import Base
from utilities.Logger import Logger

class Finish_page(Base):

    def __init__(self, driver):
        super().__init__(driver);
        self.driver = driver;

    #Locators
    price_of_product_1 = "//div[text()='Sauce Labs Backpack']/ancestor::div[@class='cart_item_label']//div[@class='inventory_item_price']"
    price_of_product_2 = "//div[text()='Sauce Labs Bike Light']/ancestor::div[@class='cart_item_label']//div[@class='inventory_item_price']"
    button_finish = "//button[@id='finish']"
    tax_filed = "//div[@class='summary_tax_label']"
    total_sum_filed_with_tax = "//div[@class='summary_total_label']"
    total_sum_filed_without_tax = "//div[@class='summary_subtotal_label']"
    finish_step_marker = "//span[@class='title']"


    #Getters
    def get_button_finish(self):
        return self.get_element_to_be_clickable_by_xpath(self.button_finish)
    def get_price_of_product_1(self):
        return self.get_visibility_of_element_located_by_xpath(self.price_of_product_1)
    def get_price_of_product_2(self):
        return self.get_visibility_of_element_located_by_xpath(self.price_of_product_2)
    def get_tax_filed(self):
        return self.get_visibility_of_element_located_by_xpath(self.tax_filed)
    def get_total_sum_filed_with_tax(self):
        return self.get_visibility_of_element_located_by_xpath(self.total_sum_filed_with_tax)
    def get_total_sum_filed_without_tax(self):
        return self.get_visibility_of_element_located_by_xpath(self.total_sum_filed_without_tax)
    def get_finish_step_marker_text(self):
        marker = self.get_visibility_of_element_located_by_xpath(self.finish_step_marker)
        return marker.text

    #Actions
    def click_button_finish(self):
        self.get_button_finish().click()
    def return_float_price(self, element):
        str_value = element.text.split("$")[1]
        return float(str_value)


    #Methods
    def get_finish_sum_product(self,):
        with allure.step("Get finish sum product"):
            Logger.add_start_step(method="Get finish sum product")
            float_product_price_1 = self.return_float_price(self.get_price_of_product_1())
            float_product_price_2 = self.return_float_price(self.get_price_of_product_2())
            product_price_sum = float_product_price_1 + float_product_price_2
            Logger.add_end_step(url=self.get_current_url(), method="Get finish sum product")
        return product_price_sum
    def assert_product_sum_without_tax(self):
        with allure.step("Assert product sum without tax"):
            Logger.add_start_step(method="Assert product sum without tax")
            float_product_price_1 = self.return_float_price(self.get_price_of_product_1())
            float_product_price_2 = self.return_float_price(self.get_price_of_product_2())
            float_total_product_sum_without_tax = self.return_float_price(self.get_total_sum_filed_without_tax())
            product_price_sum_without_tax = float_product_price_1 + float_product_price_2
            assert float_total_product_sum_without_tax == product_price_sum_without_tax
            Logger.add_end_step(url=self.get_current_url(), method="Assert product sum without tax")
    def assert_product_sum_with_tax(self):
        with allure.step("Assert product sum with tax"):
            Logger.add_start_step(method="Assert product sum with tax")
            float_product_price_1 = self.return_float_price(self.get_price_of_product_1())
            float_product_price_2 = self.return_float_price(self.get_price_of_product_2())
            float_tax_value = self.return_float_price(self.get_tax_filed())
            product_price_sum_with_tax = float_product_price_1 + float_product_price_2 + float_tax_value
            float_total_sum_value = self.return_float_price(self.get_total_sum_filed_with_tax())
            assert product_price_sum_with_tax == float_total_sum_value
            Logger.add_end_step(url=self.get_current_url(), method="Assert product sum with tax")

    def complete_test_way(self):
        with allure.step("Complete test way"):
            Logger.add_start_step(method="Complete test way")
            self.click_button_finish()
            self.assert_element_text('CHECKOUT: COMPLETE!', self.get_finish_step_marker_text())
            Logger.add_end_step(url=self.get_current_url(), method="Complete test way")