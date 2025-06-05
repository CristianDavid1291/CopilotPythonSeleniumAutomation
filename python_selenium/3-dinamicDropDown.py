import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element("id", "autosuggest").send_keys("ind")
time.sleep(2)
suggestions =  driver.find_elements("css selector", "li.ui-menu-item a")
print(suggestions)
next(suggestion.click() for suggestion in suggestions if suggestion.text == "India")
