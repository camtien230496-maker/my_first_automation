# ...existing code...
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


def test_drag_5000_to_debit_amount():
    url = "https://demo.guru99.com/test/drag_drop.html"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(5)

    original = driver.current_window_handle
    links = driver.find_elements(By.XPATH, "//a[@target='_blank']")
    if links:
        links[0].click()
        while len(driver.window_handles) < 2:
            time.sleep(0.3)
        new = [h for h in driver.window_handles if h != original][0]
        driver.switch_to.window(new)
        driver.maximize_window()
        driver.get(url)  # ensure the drag-drop page is loaded in the new tab

    srcs = driver.find_elements(By.XPATH, "//a[normalize-space()='5000']")
    tgts = driver.find_elements(By.XPATH, "//ol[@id='amt7'] | //ol[contains(@class,'placeholder')][1]")

    if srcs and tgts:
        ActionChains(driver).drag_and_drop(srcs[0], tgts[0]).perform()

    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    test_drag_5000_to_debit_amount()