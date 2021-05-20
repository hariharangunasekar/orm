import pytest
from selenium import webdriver
from PageObjects.Loginpage import LoginPage
from Utilities.readproperties import ReadConfig

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationurl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    def test_homepagetitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        title = self.driver.title
        if title =="OrangeHR":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepagetitle.png")
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        title = self.driver.title

        if title =="OrangeHRM":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False







