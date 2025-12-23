# from selenium import webdriver
# from selenium.webdriver.common.by import By 
# from selenium.webdriver.common.keys import Keys
# import pytest
# from time import sleep
# import csv

# class TestSearchWiki:
    
#     def read_data_from_file(file_path):
#         with open(file_path, mode="r") as file:
#             csv_reader = csv.DictReader(file)
#             keyword = []     #keyword=["selenium","wikipedia","cafef","veitnamnet"]
#             for row in csv_reader:
#                 keyword.append(row['keyword'])
#             return keyword
#     testdata = read_data_from_file("data.csv")
    
#     @pytest.mark.parametrize("keyword", testdata)
#     def test_search_wikipedia(self, driver, keyword): #phải đặt tên bắt đầu bằng test_
#         search_box = driver.find_element(By.NAME, "search")
#         search_box.send_keys(keyword)
#         search_box.send_keys(Keys.ENTER)
#         sleep(5)
