import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        self.driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()

        windowsOpened = self.driver.window_handles

        self.driver.switch_to.window(windowsOpened[1])
        print(self.driver.find_element(By.TAG_NAME, "h1").text)

        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com")).perform()
        print(self.driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text)

        self.driver.switch_to.window(windowsOpened[0])
        self.driver.find_element(By.ID, "username").send_keys("mentor@rahulshettyacademy.com")
        self.driver.find_element(By.NAME, "password").send_keys("123")

        checkboxes = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        checkboxes[0].click()

        self.driver.find_element(By.ID, "signInBtn").click()

        time.sleep(2)

        message = self.driver.find_element(By.CLASS_NAME, "alert-danger").text
        print(message)

        assert "Incorrect username/password" in message


