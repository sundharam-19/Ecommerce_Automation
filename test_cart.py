from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage

def test_cart_operations(setup):

    driver = setup
    driver.get("https://www.saucedemo.com/")

    lp = LoginPage(driver)

    lp.enter_username("standard_user")
    lp.enter_password("secret_sauce")
    lp.click_login()

    pp = ProductsPage(driver)

    assert driver.find_element(*pp.cart_icon).is_displayed()

    pp.select_random_products()

    assert pp.get_cart_count() == "4"

    pp.click_cart()

    cp = CartPage(driver)

    assert len(cp.get_cart_items()) == 4