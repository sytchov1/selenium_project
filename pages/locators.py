from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_COST = (By.CSS_SELECTOR, ".product_main > .price_color")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    MESSAGE_PRODUCT_COST = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, "btn-add-to-basket")