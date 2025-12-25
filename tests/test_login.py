from selenium import webdriver
from selenium.webdriver.common.by import By 
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
import pytest
from time import sleep

class TestLogin():
    def test_login_pass(self,driver):
        login = LoginPage(driver)
        login.do_login(ConfigReader.get_username(),ConfigReader.get_password())
        assert driver.find_element(By.XPATH, "//h6").text == 'Dashboard'
    
    # def test_login_wrong_password(self,driver):
    #     login = LoginPage(driver)
    #     login.do_login("Admin","admin124")
    #     assert driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")

    # def test_login_wrong_username(self,driver):
    #     login = LoginPage(driver)
    #     login.do_login("asdd","admin123")
    #     assert driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
    
    # def test_login_wrong_username_password(self, driver):
    #     login = LoginPage(driver)
    #     login.do_login("asdffdf","23686efhd")
    #     assert driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")

