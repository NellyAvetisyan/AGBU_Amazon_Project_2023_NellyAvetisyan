import unittest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilities_.customListener import MyListener
from pages_.loginPage_.loginPage import LoginPage
from time import sleep
from testData_.testData import validUser, signInPageUrl


class BaseTestWithoutLogin(unittest.TestCase):

    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get(signInPageUrl)
        sleep(20)  # to avoid check message

    def tearDown(self):
        self.driver.close()

class BaseTestWithLogin(unittest.TestCase):
    def setUp(self):
        self.simpleDriver = webdriver.Chrome()
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get(signInPageUrl)
        sleep(20) #to avoid check message
        loginPageObj = LoginPage(self.simpleDriver)
        loginPageObj.fill_username_field(validUser.username)
        loginPageObj.click_to_continue_button()
        loginPageObj.fill_password_field(validUser.password)
        sleep(6)  # to avoid CAPTCHA check
        loginPageObj.click_to_signin_button()
        sleep(15) # to avoid CAPTCHA check

    def tearDown(self):
        self.driver.close()

