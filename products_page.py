import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductsPage:

    inventory_items = (By.CLASS_NAME, "inventory_item")
    add_buttons = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    product_names = (By.CLASS_NAME, "inventory_item_name")
    product_prices = (By.CLASS_NAME, "inventory_item_price")
    sort_dropdown = (By.CLASS_NAME, "product_sort_container")

    def __init__(self, driver):
        self.driver = driver

    def select_random_products(self):
        buttons = self.driver.find_elements(*self.add_buttons)
        selected = random.sample(buttons, 4)

        for item in selected:
            item.click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_badge).text

    def click_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def sort_products(self, visible_text):
        dropdown = Select(self.driver.find_element(*self.sort_dropdown))
        dropdown.select_by_visible_text(visible_text)
