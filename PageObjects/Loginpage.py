from selenium import webdriver

class LoginPage:
    text_box_username = "//input[@id='txtUsername']"
    text_box_password = "//input[@id='txtPassword']"
    login_button = "//input[@id='btnLogin']"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element_by_xpath(self.text_box_username).clear()
        self.driver.find_element_by_xpath(self.text_box_username).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.text_box_password).clear()
        self.driver.find_element_by_xpath(self.text_box_password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.login_button).click()



