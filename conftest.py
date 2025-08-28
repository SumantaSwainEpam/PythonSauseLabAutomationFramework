from threading import Thread

import pytest
import os
from datetime import datetime
from drivers.driver_factory import DriverFactory
from utilities.screenshots import take_screenshot
from utilities.report_manager import ReportManager
from utilities.logger_manager import LoggerManager

pytest_html = None

# Create report directory and log it
report_dir = ReportManager.create_report_directory()
logger = LoggerManager.get_logger("TestExecution")
logger.info(f"Report directory created at: {report_dir}")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use for testing")

@pytest.fixture(scope="function")
def driver(request):
    try:
        browser = request.config.getoption("browser")
    except Exception:
        browser = "chrome"

    logger.info(f"Starting test: {request.node.name} on browser: {browser}")
    _driver = DriverFactory.get_driver(browser)
    request.node.driver = _driver

    try:
        yield _driver
    finally:
        DriverFactory.quit_driver()
        logger.info(f"Finished test: {request.node.name} and closed browser")

def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")

    if not os.path.exists("reports"):
        os.makedirs("reports")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = os.path.join("reports", f"Test_Report_{timestamp}.html")

    config._metadata = {
        "Project": "Sauce Demo POM Tests",
        "Browser": config.getoption("--browser"),
        "Generated On": timestamp
    }

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":
        if rep.failed:
            driver = getattr(item, "driver", None)
            if driver:
                screenshot_path = take_screenshot(driver, item.name)
                logger.error(f"Test failed: {item.name}. Screenshot saved at: {screenshot_path}")

                if screenshot_path:
                    rel_path = os.path.relpath(screenshot_path, start=os.path.dirname(report_dir))
                    extra_html = f'<div><a href="{rel_path}" target="_blank">' \
                                 f'<img src="{rel_path}" alt="screenshot" style="height:150px;border:1px solid #ccc"/></a></div>'
                    if hasattr(rep, "extra"):
                        rep.extra.append(pytest_html.extras.html(extra_html))
                    else:
                        rep.extra = [pytest_html.extras.html(extra_html)]

        elif rep.passed:
            logger.info(f"Test passed: {item.name}")
        elif rep.skipped:
            logger.warning(f"Test skipped: {item.name}")
