
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class AddProduct(BasePage):

    #Locators
    # product_links = [
    #     (By.CSS_SELECTOR, "#item_4_title_link"),  # SauceLabsBackpack
    #     (By.CSS_SELECTOR, "#item_0_title_link"),  # SauceLabsBikeLight
    #     (By.CSS_SELECTOR, "#item_1_title_link"),  # SauceLabsBoltTShirt
    #     (By.CSS_SELECTOR, "#item_5_title_link"),  # SauceLabsFleeceJacket
    #     (By.CSS_SELECTOR, "#item_2_title_link"),  # SauceLabsOnesie
    #     (By.CSS_SELECTOR, "#item_3_title_link")   # SauceLabTShirtRed
    # ]

    AddToCart=(By.CSS_SELECTOR,"button.btn_inventory")
    BackToProducts=(By.XPATH,'//button[@id="back-to-products"]')

    SauceLabsBackpack= (By.CSS_SELECTOR, "#item_4_title_link")  # SauceLabsBackpack
    SauceLabsBikeLight=(By.CSS_SELECTOR, "#item_0_title_link") # SauceLabsBikeLight

    #constructor
    def __init__(self,driver):
        super().__init__(driver)

    def select_products(self):
        # Get and click product
        product_element = self.get_element(self.SauceLabsBackpack)
        self.scroll_to_element(product_element)
        self.click(product_element)

        # Add to cart
        self.wait_for_element(self.AddToCart, "clickable")
        self.click(self.AddToCart)

        # Back to product listing
        self.wait_for_element(self.BackToProducts, "clickable")
        self.click(self.BackToProducts)



    # def select_all_products(self):
    #     products=self.get_elements_from_list(self.product_links)
    #     for product in products:
    #         if product is not None:
    #             self.wait_for_element(self.product,"visible")
    #             self.scroll_to_element(self.product)
    #             self.click(product)
    #             self.click(self.AddToCart)
    #             self.click(self.BackToProducts)
