from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("tests")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("tests")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("tests@tests.com")

    button1 = browser.find_element(By.ID, "file")
    button1.send_keys("C:/Users/By9ln/PycharmProjects/pythonProject/venv/Scripts/tests.txt")

    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
