from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory:
    _driver = None

    @staticmethod
    def get_driver(browser_name="chrome"):
        if DriverFactory._driver is None:
            browser = browser_name.lower()
            if browser == "chrome":
                options = webdriver.ChromeOptions()
                options.add_argument("--start-maximized")
                # options.add_argument("--headless")
                service = ChromeService(ChromeDriverManager().install())
                DriverFactory._driver = webdriver.Chrome(service=service, options=options)

            elif browser == "firefox":
                options = webdriver.FirefoxOptions()
                options.add_argument("--start-maximized")
                # options.add_argument("--headless")
                service = FirefoxService(GeckoDriverManager().install())
                DriverFactory._driver = webdriver.Firefox(service=service, options=options)

            elif browser == "edge":
                options = webdriver.EdgeOptions()
                options.add_argument("--start-maximized")
                service = EdgeService(EdgeChromiumDriverManager().install())
                DriverFactory._driver = webdriver.Edge(service=service, options=options)

            else:
                raise ValueError(f"Browser '{browser_name}' is not supported.")

        return DriverFactory._driver

    @staticmethod
    def quit_driver():
        if DriverFactory._driver:
            DriverFactory._driver.quit()
            DriverFactory._driver = None
