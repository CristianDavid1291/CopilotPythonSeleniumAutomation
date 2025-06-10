from selenium import webdriver
import os
import sys
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from python_pageObjects.login import LoginPage

def test_loginE2e(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginPage = LoginPage(driver)
    loginPage.login()
    time.sleep(3)  # Wait for the login to complete


