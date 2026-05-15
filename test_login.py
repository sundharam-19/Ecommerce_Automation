import pytest
import time

from login_page import LoginPage


@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
        ("locked_out_user", "secret_sauce"),
        ("invalid_user", "wrong_pass")
    ]
)

def test_login(setup, username, password):

    driver = setup

    driver.get("https://www.saucedemo.com/")

    time.sleep(2)

    lp = LoginPage(driver)

    lp.enter_username(username)
    lp.enter_password(password)
    lp.click_login()

    time.sleep(2)

    if username == "locked_out_user":

        assert "Epic sadface" in driver.page_source

    elif username == "invalid_user":

        assert "Epic sadface" in driver.page_source

    else:

        assert "inventory" in driver.current_url