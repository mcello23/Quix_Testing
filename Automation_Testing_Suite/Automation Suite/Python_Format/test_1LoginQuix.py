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

class Test1LoginQuix():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_1LoginQuix(self):
    # Test name: 1-LoginQuix
    # Step # | name | target | value
    # 1 | open | | 
    self.driver.get("")
    # 2 | setWindowSize | 2072x1392 | 
    self.driver.set_window_size(2072, 1392)
    # 3 | click | css=.auth0-lock-center | 
    self.driver.find_element(By.CSS_SELECTOR, ".auth0-lock-center").click()
    # 4 | click | id=1-email | 
    self.driver.find_element(By.ID, "1-email").click()
    # 5 | type | id=1-email | 
    self.driver.find_element(By.ID, "1-email").send_keys("")
    # 6 | click | css=.auth0-lock-center | 
    self.driver.find_element(By.CSS_SELECTOR, ".auth0-lock-center").click()
    # 7 | click | name=password | 
    self.driver.find_element(By.NAME, "password").click()
    # 8 | type | name=password | 
    self.driver.find_element(By.NAME, "password").send_keys("")
    # 9 | click | css=.auth0-label-submit | 
    self.driver.find_element(By.CSS_SELECTOR, ".auth0-label-submit").click()
    # 10 | click | css=div > .text-truncate:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, "div > .text-truncate:nth-child(1)").click()
    # 11 | click | css=.mat-list-item:nth-child(2) > .mat-list-item-content | 
    self.driver.find_element(By.CSS_SELECTOR, ".mat-list-item:nth-child(2) > .mat-list-item-content").click()
    # 12 | close |  | 
    # Not part of the scope but wanted to automate this
    self.driver.close()
  
