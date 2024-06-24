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

class TestGetSmellByDate():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_getSmellByDate(self):
    self.driver.get("http://localhost:3000/chatbot")
    self.driver.set_window_size(1512, 945)
    self.driver.find_element(By.CSS_SELECTOR, "input").click()
    self.driver.find_element(By.CSS_SELECTOR, "input").send_keys("ciao cadocs potresti trovare gli smells qui https://github.com/gianwario/BeeHave a partire dal 12/01/2023")
    self.driver.find_element(By.CSS_SELECTOR, "input").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".bot > div").click()
    self.driver.find_element(By.CSS_SELECTOR, "input").click()
  