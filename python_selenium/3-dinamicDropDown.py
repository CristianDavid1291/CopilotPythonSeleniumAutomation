import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element("id", "autosuggest").send_keys("ind")
time.sleep(2)
suggestions =  driver.find_elements("css selector", "li.ui-menu-item a")
print(suggestions)
next(suggestion.click() for suggestion in suggestions if suggestion.text == "India")


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements("css selector", "input[id*='checkBox']")

next(checkbox.click() for checkbox in checkboxes if checkbox.get_attribute("value") == "option2")
time.sleep(2)
