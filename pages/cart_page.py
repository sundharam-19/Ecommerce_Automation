from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    cart_items = (By.CLASS_NAME, "cart_item")
    checkout_btn = (By.ID, "checkout")

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def get_cart_items(self):

        return self.driver.find_elements(
            *self.cart_items
        )

    def click_checkout(self):

        checkout = self.wait.until(
            EC.presence_of_element_located(
                self.checkout_btn
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            checkout
        )