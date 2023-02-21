import time
import allure

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.Cart_page import Cart_page
from pages.Catalog_page import Catalog_page
from pages.Login_page import Login_page

@allure.description("test_buy_product")
def test_action(set_up):

    driver = webdriver.Chrome(ChromeDriverManager().install())
    path_to_screenshot = "..\\screen\\"
    username = "standard_user"
    password = "secret_sauce"

    login_page = Login_page(driver)
    login_page.authorization(username, password)
    login_page.screen_page(path_to_screenshot)

    catalog_page = Catalog_page(driver)
    product_price_sum = catalog_page.add_to_cart_two_products_and_return_sum_price()

    cart_page = Cart_page(driver)
    product_price_sum_in_cart = cart_page.get_sum_product()
    cart_page.action_checkout()

    assert product_price_sum == product_price_sum_in_cart

    time.sleep(2)
    driver.close()