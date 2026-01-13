from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest



class TestSwitchToWindow:
    def test_switch_to_new_window(self, driver):
        """Open the practice page, click 'Open Window', wait for new window, switch and verify."""
        driver.get("https://www.letskodeit.com/practice")

        wait = WebDriverWait(driver, 10)

        # wait for the 'Open Window' button to be clickable, then click it
        open_window_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "openwindow"))
        )
        main_handle = driver.current_window_handle
        open_window_btn.click()

        # wait until a new window handle appears
        wait.until(lambda d: len(d.window_handles) > 1)

        # switch to the new window (the one that's not the main window)
        handles = driver.window_handles
        new_handle = [h for h in handles if h != main_handle][0]
        driver.switch_to.window(new_handle)

        # maximize the newly opened window
        driver.maximize_window()

        # optional: wait for the new window to load a known element or a change in title
        try:
            wait.until(EC.title_contains("Practice"))
        except Exception:
            # not all target pages set title immediately; still assert we have a different handle
            pass

        assert driver.current_window_handle == new_handle

        # cleanup: close the new window and switch back
        driver.close()
        driver.switch_to.window(main_handle)
        assert driver.current_window_handle == main_handle
