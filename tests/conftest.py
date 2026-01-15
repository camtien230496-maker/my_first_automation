import pytest
from selenium import webdriver
from utils.config_reader import ConfigReader

@pytest.fixture(scope="function")
def driver():
    #Đây là setup driver cho các test script dùng & chỉ setup 1 lần duy nhất

    driver = webdriver.Chrome()
    driver.implicitly_wait(10) #thời gian chờ tương tác với mỗi text box
    driver.maximize_window()
    # base_url = "https://the-internet.herokuapp.com/dropdown"
   
    base_url = ConfigReader.get_base_url()

    # base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    # url = "https://vi.wikipedia.org"

    driver.get(base_url)
    yield driver
    #yield: đợi chạy xong TS rồi mới quit
    #Đây là phần teardown cho mỗi test script
    driver.quit()