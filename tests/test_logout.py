from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout(setup):

    driver = setup
    wait = WebDriverWait(driver, 20)

    driver.get("https://www.saucedemo.com/")

    lp = LoginPage(driver)

    lp.enter_username("standard_user")
    lp.enter_password("secret_sauce")
    lp.click_login()

    wait.until(
        EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
    ).click()

    wait.until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    ).click()

    assert "saucedemo" in driver.current_url

