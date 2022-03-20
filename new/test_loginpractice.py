from lib2to3.pgen2 import driver

import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utilites.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_login(self):
        log = self.getLogger()
        email = self.driver.find_element(By.CSS_SELECTOR, "#email_field")
        email.send_keys('dineshkumarav07@gmail.com')
        log.info("Entering Email")

        # Enter Password
        password = self.driver.find_element(By.CSS_SELECTOR, "#password_field")
        password.send_keys('Demondemo@1')
        log.info("Entering Password")

        # Click Login
        button = self.driver.find_element(By.CSS_SELECTOR, "#login1").click()
        log.info("Clicking log-in button")

        textmatch = (self.driver.find_element(By.CSS_SELECTOR, "#root > div:nth-child(2) > nav > div.jss24 > div > div > div > nav.MuiList-root-709.MuiList-padding-710.MuiList-subheader-712 > div.MuiButtonBase-root-727.MuiListItem-root-719.MuiListItem-gutters-724.MuiListItem-button-725.jss18 > div.MuiListItemText-root-730 > span").text)

        log.info("Successfully logged into konfhub")