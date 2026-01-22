
import pytest
from selenium import webdriver
from utils.config_reader import ConfigReader
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.chrome.service import Service 


@pytest.fixture(scope="function")
def driver():
    #Đây là setup driver cho các test script dùng & chỉ setup 1 lần duy nhất
    options = Options()
    if headless := ConfigReader.get_headless():
        options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10) #thời gian chờ tương tác với mỗi text box
    driver.maximize_window()
    base_url = ConfigReader.get_base_url()
    driver.get(base_url)
    
    yield driver
    #yield: đợi chạy xong TS rồi mới quit
    #Đây là phần teardown cho mỗi test script
    driver.quit()

