from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

class TestDemoqaHover:
    def test_hover_sub_menu(self, driver):
        driver.get("https://demoqa.com/menu")
        wait = WebDriverWait(driver, 10)
        actions = ActionChains(driver)

        # đợi menu chính xuất hiện và hover vào nó
        main_item = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Main Item 2']")))
        actions.move_to_element(main_item).perform()

        # đợi sub-menu hiện ra rồi hover vào sub-item (ví dụ 'Sub Item' hoặc 'Sub Sub Item 1')
        sub_item = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Sub Item']")))
        actions.move_to_element(sub_item).perform()

        # giữ 5 giây để quan sát
        time.sleep(5)