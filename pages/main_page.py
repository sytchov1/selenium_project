from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, browser, url, timeout=10) -> None:
        super().__init__(browser, url, timeout=timeout)