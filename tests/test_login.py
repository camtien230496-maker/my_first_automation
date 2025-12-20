from selenium import webdriver
from selenium.webdriver.common.by import By 
import pytest
from time import sleep

def test_login(driver):

    driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin") #By.XPATH
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
    #click button login
    driver.find_element(By.XPATH, "//button[@type='submit']").click() 
    sleep(5)
    assert driver.find_element(By.XPATH, "//h6").text == 'Dashboard'
    
