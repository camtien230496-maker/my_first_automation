# from selenium import webdriver
# from selenium.webdriver.common.by import By 
# from selenium.webdriver.common.keys import Keys
# import pytest
# from time import sleep
# import csv
# import os


# def read_data_from_file(file_name):

#     current_dir = os.path.dirname(os.path.abspath(__file__))
#     file_path = os.path.join(current_dir, file_name)

#     with open(file_path, mode="r", encoding="utf-8") as file:
#         csv_reader = csv.DictReader(file)
#         keywords = []
#         for row in csv_reader:
#             keywords.append(row["keyword"])
#     return keywords

# testdata = read_data_from_file("data.csv")

# @pytest.mark.parametrize("keyword", testdata)
# def test_search_wikipedia(driver, keyword):
#     driver = webdriver.Chrome()
#     driver.get("https://vi.wikipedia.org")
#     search_box = driver.find_element(By.NAME, "search")
#     search_box.clear()
#     search_box.send_keys(keyword)
#     search_box.send_keys(Keys.ENTER)
#     sleep(5)