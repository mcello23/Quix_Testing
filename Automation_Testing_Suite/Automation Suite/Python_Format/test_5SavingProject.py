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

class Test5SavingProject():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_5SavingProject(self):
    # Test name: 5-SavingProject
    # Step # | name | target | value
    # 1 | open | | 
    self.driver.get("")
    # 2 | setWindowSize | 2044x1392 | 
    self.driver.set_window_size(2044, 1392)
    # 3 | click | css=.mat-list-item:nth-child(2) > .mat-list-item-content | 
    self.driver.find_element(By.CSS_SELECTOR, ".mat-list-item:nth-child(2) > .mat-list-item-content").click()
    # 4 | click | css=div > .text-truncate:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, "div > .text-truncate:nth-child(1)").click()
    # 5 | click | css=.mat-basic > .mat-button-wrapper | 
    self.driver.find_element(By.CSS_SELECTOR, ".mat-basic > .mat-button-wrapper").click()
    # 6 | click | css=.mat-button-wrapper span | 
    self.driver.find_element(By.CSS_SELECTOR, ".mat-button-wrapper span").click()
    # 7 | click | css=.mat-button-wrapper span | 
    self.driver.find_element(By.CSS_SELECTOR, ".mat-button-wrapper span").click()
    # 8 | click | css=.text-small | 
    self.driver.find_element(By.CSS_SELECTOR, ".text-small").click()
    # 9 | click | css=.mat-h1 | 
    self.driver.find_element(By.CSS_SELECTOR, ".mat-h1").click()
    # 10 | assertTitle | css=.py-2:nth-child(2) | Demo Data - Source
    assert self.driver.title == "css=.py-2:nth-child(2)"
  
