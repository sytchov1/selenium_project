from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT), "There is the product in the basket, and it should be empty"

    def should_be_basket_empty_message(self):
        assert "Your basket is empty" in self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text, "Basket empty message is not presented, but it should be"