import time
import allure

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.Cart_page import Cart_page
from pages.Catalog_page import Catalog_page
from pages.Client_info_page import Client_info_page
from pages.Finish_page import Finish_page
from pages.Login_page import Login_page
from utilities.Logger import Logger


@allure.description("test_buy_two_product_way")
def test_buy_two_product_way(driver):
    Logger.add_start_step(method="Проверка всего пути покупки двух товаров")
    path_to_screenshot = "screen\\"
    username = "standard_user"
    password = "secret_sauce"
    first_name = "Evgeny"
    last_name = "Silkin"
    zip_postal_code = "460033"

    login_page = Login_page(driver)
    login_page.authorization(username, password)
    login_page.screen_page(path_to_screenshot)

    catalog_page = Catalog_page(driver)
    product_price_sum = catalog_page.add_to_cart_two_products_and_return_sum_price()

    cart_page = Cart_page(driver)
    product_price_sum_on_cart = cart_page.get_sum_product()
    cart_page.action_checkout()

    assert product_price_sum == product_price_sum_on_cart

    client_info_page = Client_info_page(driver)
    client_info_page.fill_client_form_and_continue(first_name, last_name, zip_postal_code)

    finish_page = Finish_page(driver)
    product_price_sum_on_finish_page = finish_page.get_finish_sum_product()

    assert product_price_sum_on_cart == product_price_sum_on_finish_page

    finish_page.assert_product_sum_without_tax()
    finish_page.assert_product_sum_with_tax()
    finish_page.complete_test_way()
    finish_page.screen_page(path_to_screenshot)

    Logger.add_end_step(url=finish_page.get_current_url(),
                        method="Проверка всего пути покупки двух товаров")