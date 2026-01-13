from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class TestSubmitForm:
    def test_login_form(self, driver):
        # navigate directly to the login page
        driver.get("https://the-internet.herokuapp.com/login")

        wait = WebDriverWait(driver, 10)

        # fill the username and password fields (wait until present)
        username = wait.until(EC.presence_of_element_located((By.ID, "username")))
        password = wait.until(EC.presence_of_element_located((By.ID, "password")))
        username.clear()
        username.send_keys("tomsmith")
        password.clear()
        password.send_keys("SuperSecretPassword!")

        # submit using the <form>.submit() method (wait for form to be present)
        form = wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))
        form.submit()

        # verify successful login - wait until the Secure Area header is visible
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h2"))).text
        assert "Secure Area" in header