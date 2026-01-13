from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest


class TestAlertAndPopup:
    def test_click_alert_and_accept(self, driver):
        driver.get("https://www.letskodeit.com/practice")
        wait = WebDriverWait(driver, 10)

        # click nút Alert (ID thường là 'alertbtn')
        wait.until(EC.element_to_be_clickable((By.ID, "alertbtn"))).click()

        # chờ alert xuất hiện
        alert = wait.until(EC.alert_is_present())
        # chờ 5 giây trước khi nhấn OK (theo yêu cầu)
        time.sleep(5)
        alert.accept()