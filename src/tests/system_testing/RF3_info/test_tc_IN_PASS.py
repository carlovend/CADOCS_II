# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTCINPASS():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tCINPASS(self):
    # Test name: TC_IN_PASS
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("http://localhost:3000/")
    # 2 | setWindowSize | 1427x763 | 
    self.driver.set_window_size(1427, 763)
    # 3 | click | id=1 | 
    self.driver.find_element(By.ID, "1").click()
    # 4 | click | css=input | 
    self.driver.find_element(By.CSS_SELECTOR, "input").click()
    # 5 | type | css=input | hey cadocs can you tell me more about the community smells you can detect?
    self.driver.find_element(By.CSS_SELECTOR, "input").send_keys("hey cadocs can you tell me more about the community smells you can detect?")
    # 6 | click | css=button | 
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    # 7 | mouseOver | css=button | 
    element = self.driver.find_element(By.CSS_SELECTOR, "button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 8 | mouseOut | css=button | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
  
