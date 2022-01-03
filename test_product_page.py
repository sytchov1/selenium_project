from .pages.product_page import ProductPage
import time
import pytest


@pytest.mark.parametrize('num', [pytest.param(num, marks=pytest.mark.xfail) if num == 7 else num for num in range(10)])
def test_guest_can_add_product_to_basket(browser, num):
    link = f"http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer{num}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_right_message()
    page.should_be_right_cost()