from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from time import sleep
from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.__username = (By.NAME, "username")
        self.__password = (By.NAME, "password")
        self.login_btn = (By.XPATH, "//button[@type='submit']")


    def enter_username(self, username):
        self.find_element(self.__username).send_keys(username)
    
    def enter_password(self, password):
        self.find_element(self.__password).send_keys(password)

    def click_login_btn(self):
        self.find_element(self.login_btn).click()

    def do_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_btn()









# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.username = (By.NAME, "username")
#         self.password = (By.NAME, "password")
#         self.login_btn = (By.XPATH, "//button[@type='submit']")
        
#     def enter_username(self, username):
#         self.driver.find_element(*self.username).send_keys(username)
        
#     def enter_password(self, password):
#         self.driver.find_element(*self.password).send_keys(password)
        
#     def click_btn_login(self):
#         self.driver.find_element(*self.login_btn).click()
        
#     def do_login(self, username, password):
#         self.enter_username(username)
#         self.enter_password(password)
#         self.click_btn_login()
        
#     def get_error_message(self, username, password):
#         self.enter_username(username)
#         self.enter_password(password)
#         self.click_btn_login()
#         return self.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    # def enter_username(self,username):
    #     self.driver1.find_element(By.NAME,)
        
    # def enter_password(self,password):
    #     self.driver1.find_element(By.NAME,)

    # def click_login_button(self):
    #     self.driver1.find_element(By.XPATH, "//button[@type='submit']").click()
    
    # def get_error_message(self):
    #     return self.driver1.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")