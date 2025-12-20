from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from time import sleep

class LoginPage:
    def __init__(self, driver):
        self.driver1 =driver
        
    def enter_username(self,username):
        self.driver1.find_element(By.NAME,)