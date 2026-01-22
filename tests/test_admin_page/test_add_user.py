from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.admin_page.user_management_page import UserManagement

class TestAddNewUser():
    def test_add_new_user(self, driver):
        user_mgmt = UserManagement(driver)
        user_mgmt.navigate_to_user_management()
        user_mgmt.add_user(
            role="ESS",
            employee_name="Linda Anderson",
            username="linda.anderson",
            status="Enabled",
            password="Password123!")

        # Verify user is added - this can be done by searching for the user in the user list
        search_input = (By.XPATH, "//input[@placeholder='Type for hints...']")
        search_btn = (By.XPATH, "//button[@type='submit']")
        user_mgmt.find_element(search_input).send_keys("linda.anderson")
        user_mgmt.click(search_btn)
        # Check if the user appears in the search results
        user_in_list = (By.XPATH, "//div[@class='oxd-table-cell oxd-padding-cell'][text()='linda.anderson']")
        assert user_mgmt.find_element(user_in_list).is_displayed()