import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import LoginPage
from products_page import ProductsPage


def test_reset_app_state(setup):

    driver = setup

    wait = WebDriverWait(driver, 20)

    driver.get("https://www.saucedemo.com/")

    lp = LoginPage(driver)

    lp.enter_username("standard_user")
    lp.enter_password("secret_sauce")
    lp.click_login()

    pp = ProductsPage(driver)

    pp.select_random_products()

    time.sleep(2)

    menu = wait.until(
        EC.presence_of_element_located(
            (By.ID, "react-burger-menu-btn")
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        menu
    )

    time.sleep(2)

    reset_btn = wait.until(
        EC.presence_of_element_located(
            (By.ID, "reset_sidebar_link")
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        reset_btn
    )

    time.sleep(2)

    driver.refresh()

    badges = driver.find_elements(
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    assert len(badges) == 0