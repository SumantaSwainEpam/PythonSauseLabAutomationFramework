from selenium.common import TimeoutException
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    #Locators
    USERNAME=(By.CSS_SELECTOR,"#user-name")
    PASSWORD=(By.CSS_SELECTOR,"#password")
    LOGIN_BUTTON=(By.CSS_SELECTOR,"#login-button")
    PRODUCTS=(By.XPATH,'''//span[@class="title" and text()="Products"]''')

    def __init__(self,driver):
        super().__init__(driver)


    def open_login_page(self,url):
        self.driver.get(url)

    def login(self,username,password):
        self.enter_text(self.USERNAME,username)
        self.enter_text(self.PASSWORD,password)
        self.click(self.LOGIN_BUTTON)

    def is_products_title_visible(self,):
        try:
            return self.is_visible(self.PRODUCTS)
        except TimeoutException:
            return False

