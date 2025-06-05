from selenium import webdriver

#driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get("https://www.google.com")
driver.close()