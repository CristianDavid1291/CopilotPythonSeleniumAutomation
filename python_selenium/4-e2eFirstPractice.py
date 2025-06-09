from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Shop").click()
products = driver.find_elements(By.CSS_SELECTOR, "div.card-body h4 a")
addBtns = driver.find_elements(By.CSS_SELECTOR, "div.card.h-100 button.btn.btn-info")
text = "iphone"

for i in range(len(products)):
    if text in products[i].text:
        addBtns[i].click()
        break

driver.find_element(By.CSS_SELECTOR, "a.nav-link.btn.btn-primary").click()
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success").click()
driver.find_element(By.CSS_SELECTOR, "input#country").send_keys("ind")
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[text()='India']"))
)
element.click()
# wair for element is not intercepted by the next line
label = WebDriverWait(driver, 10).until(    
    EC.presence_of_element_located((By.CSS_SELECTOR, "label[for='checkbox2']"))
)
label.click()
driver.find_element(By.CSS_SELECTOR, "input.btn.btn-success.btn-lg").click()
successText = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible").text
assert "Success! Thank you!" in successText, "Success message not found"
print("Test passed successfully")   




