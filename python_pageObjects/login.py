from selenium.webdriver.common.by import By


class LoginPage:

    
    def __init__(self, driver):
        self.driver = driver
        self.usernameTxt = (By.ID, "username")
        self.passwordTxt = (By.ID, "password")
        self.termsCheck = (By.ID, "terms")
        self.sigInBtn = (By.ID, "signInBtn")

    def login(self):
        self.driver.find_element(*self.usernameTxt).send_keys("testuser")
        self.driver.find_element(*self.passwordTxt).send_keys("testpass")
        self.driver.find_element(*self.termsCheck).click()
        self.driver.find_element(*self.sigInBtn).click()

        