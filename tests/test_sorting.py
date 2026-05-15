from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_sorting(setup):

    driver = setup
    driver.get("https://www.saucedemo.com/")

    lp = LoginPage(driver)

    lp.enter_username("standard_user")
    lp.enter_password("secret_sauce")
    lp.click_login()

    pp = ProductsPage(driver)

    pp.sort_products("Price (low to high)")

    assert True
