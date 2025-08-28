import pytest
from conftest import driver
from pages.login_page import LoginPage
from utilities.data_reader import load_test_data
from utilities.logger_manager import LoggerManager

test_data=load_test_data()
base_url=test_data["base_url"]
logger = LoggerManager.get_logger("LoginTest")


@pytest.mark.parametrize("user_type",["valid_user","invalid_user"])
def test_login_scenario(driver,user_type):
    login_page=LoginPage(driver)

    logger.info(f"Starting login test for user type: {user_type}")
    logger.info(f"Navigating to {base_url}")
    login_page.open_login_page(base_url)

    logger.info(f"Using credentials: {'username'} / {'*' * len('password')}")
    username=test_data[user_type]["username"]
    password=test_data[user_type]["password"]

    logger.info('login to the sauce-lab page')
    login_page.login(username,password)

    if user_type == "valid_user":
        assert login_page.is_products_title_visible(),"Log in failed: Products title is not visible"
        logger.info("Login successful. 'Products' title is visible.")
    else:
        assert not login_page.is_products_title_visible(), "Invalid user should not see 'Products' title"
        logger.info("Invalid login handled correctly. 'Products' title not visible.")
