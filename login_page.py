from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    txt_username = (By.ID, "user-name")
    txt_password = (By.ID, "password")
    btn_login = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def enter_username(self, username):

        self.wait.until(
            EC.visibility_of_element_located(
                self.txt_username
            )
        ).send_keys(username)

    def enter_password(self, password):

        self.wait.until(
            EC.visibility_of_element_located(
                self.txt_password
            )
        ).send_keys(password)

    def click_login(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.btn_login
            )
        ).click()
