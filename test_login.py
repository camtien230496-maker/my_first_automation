from selenium import webdriver
from selenium.webdriver.common.by import By 
import pytest
from time import sleep

def test_login():
    driver = webdriver.Chrome()
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver.get(base_url)
    #phong to SUT
    driver.maximize_window()
    #wait for SUT fully loaded
    sleep(5)
    driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin") #By.XPATH
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
    #click button login
    driver.find_element(By.XPATH, "//button[@type='submit']").click() 
    sleep(5)
    assert driver.find_element(By.XPATH, "//h6").text == 'Dashboard'
    
