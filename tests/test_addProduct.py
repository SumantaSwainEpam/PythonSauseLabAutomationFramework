
from pages.add_product import AddProduct
from utilities import login_helper
from conftest import driver


def test_add_products(driver):
    login_helper.login_as_valid_user(driver)
    add_product = AddProduct(driver)
    #add_product.select_all_products()
    add_product.select_products()
