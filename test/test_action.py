import time
import allure

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.Name_page import Name_page

@allure.description("test_buy_product")
def test_action(set_up):


    driver = webdriver.Chrome(ChromeDriverManager().install())
    # path_to_screenshot = "D:\\IT\\QA\\Auto\\Python\\AutoTestingSelenium\\screen\\"
    path_to_screenshot = "..\\screen\\"

    name_page = Name_page(driver)
    name_page.authorization()
    name_page.screen_page(path_to_screenshot)

    time.sleep(2)
    driver.close()