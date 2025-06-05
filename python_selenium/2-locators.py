from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

#ID, xpath, className, tagName, name, linkText, partialLinkText, cssSelector
driver.find_element(By.NAME, "email").send_keys("cristiandavid1291@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456789")
driver.find_element(By.ID, "exampleCheck1").click()
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
driver.find_element(By.CSS_SELECTOR, "input.btn.btn-success[value='Submit']").click()
message = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-success").text
print(message)
assert "Success" in message, "Message does not contain 'Success'"

