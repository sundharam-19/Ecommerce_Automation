from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_checkout(setup):

    driver = setup
    wait = WebDriverWait(driver, 20)

    driver.get("https://www.saucedemo.com/")

    lp = LoginPage(driver)
    lp.enter_username("standard_user")
    lp.enter_password("secret_sauce")
    lp.click_login()

    pp = ProductsPage(driver)

    # Add products
    pp.select_random_products()

    # Open cart
    driver.get("https://www.saucedemo.com/cart.html")

    # Checkout
    checkout_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_btn.click()

    # Fill details
    wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    ).send_keys("Sundharam")

    driver.find_element(By.ID, "last-name").send_keys("Test")
    driver.find_element(By.ID, "postal-code").send_keys("600001")

    driver.find_element(By.ID, "continue").click()

    # Finish order
    finish_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "finish"))
    )

    driver.execute_script(
        "arguments[0].scrollIntoView();",
        finish_btn
    )

    driver.execute_script(
        "arguments[0].click();",
        finish_btn
    )

    # Confirmation
    confirmation = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "complete-header")
        )
    ).text

    assert "Thank you" in confirmation
