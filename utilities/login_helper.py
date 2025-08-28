from pages.login_page import LoginPage
from utilities.data_reader import load_test_data
from utilities.logger_manager import LoggerManager


def login_as_valid_user(driver):
    #Logger
    logger = LoggerManager.get_logger("LoginWithValidUserTest")

    # Load test data
    test_data = load_test_data()
    base_url = test_data["base_url"]
    username = test_data["valid_user"]["username"]
    password = test_data["valid_user"]["password"]

    # Perform login
    login_page = LoginPage(driver)
    logger.info(f"Navigating to {base_url}")
    login_page.open_login_page(base_url)
    logger.info(f"Using credentials: {username} / {'*' * len(password)}")

    logger.info('Logging in to the Sauce Demo site...')
    login_page.login(username, password)
