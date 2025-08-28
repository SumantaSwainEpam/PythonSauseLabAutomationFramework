from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver= driver
        self.wait=WebDriverWait(self.driver,10)

    def click(self,by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def enter_text(self ,by_locator,text):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self,by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).text

    def is_visible(self,by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).is_displayed()

    def get_element(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def get_elements(self, by_locator):
        return self.driver.find_elements(*by_locator)

    def get_elements_from_list(self, locator_list):
        elements = []
        for locator in locator_list:
            try:
                element = self.wait.until(EC.presence_of_element_located(locator))
                elements.append(element)
            except TimeoutException:
                print(f"[Warning] Element not found for locator: {locator}")
                elements.append(None)
        return elements

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)


    def wait_for_element(self, locator, condition="visible", timeout=10):
        try:
            if condition == "visible":
                return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            elif condition == "clickable":
                return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            elif condition == "present":
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print(f"[Timeout] Element not found or not {condition}: {locator}")
            return None