from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN).click()

    def should_be_right_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_product_name = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        assert product_name == message_product_name, "Product name in message is not the same as product name in page"

    def should_be_right_cost(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        message_product_cost = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_COST).text
        assert product_cost == message_product_cost, "Product cost in message is not the same as product cost in page"