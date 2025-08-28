import os
from datetime import datetime

def take_screenshot(driver, name):
    screenshots_dir = os.path.join(os.getcwd(), "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_fail_{timestamp}.png"
    file_path = os.path.join(screenshots_dir, filename)

    driver.save_screenshot(file_path)
    print(f"[Screenshot saved] → {file_path}")
    return file_path
