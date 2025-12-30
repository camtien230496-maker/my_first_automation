from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException



def test_setup(driver):
    select = Select(driver.find_element(By.ID, "dropdown"))
    select.select_by_visible_text("Option 1") 
    sleep(3)
    select.select_by_value("2")
    sleep(3)
        
    