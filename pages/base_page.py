from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class BasePage:
    def __init__ (self, driver):
        self.driver = driver
        
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def click(self, locator):
        element = self.find_element(locator)
        try:
            element.click()
        except NoSuchElementException:
            element = self.wait_for_element_clickable(locator)
            element.click()
    
    def wait_for_element_clickable(self, locator, timeout=None):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))
    
    def move_to_element(self, locator):
        element = self.find_element(locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def dropdown_select_by_visible_text(self, locator, text):
        dropdown = Select(self.find_element(locator))
        dropdown.select_by_visible_text(text)

    def dropdown_select_by_value(self, locator, value):
        dropdown = Select(self.find_element(locator))
        dropdown.select_by_value(value)
    
        