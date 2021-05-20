from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path='D:\driver\chromedriver_win32\chromedriver.exe')
    return driver