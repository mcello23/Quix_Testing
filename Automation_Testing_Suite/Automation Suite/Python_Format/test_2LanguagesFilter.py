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

class Test2LanguagesFilter():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_2LanguagesFilter(self):
    # Test name: 2-LanguagesFilter
    # Step # | name | target | value
    # 1 | open | | 
    self.driver.get("")
    # 2 | setWindowSize | 2044x1392 | 
    self.driver.set_window_size(2044, 1392)
    # 3 | click | css=.mat-list-item:nth-child(2) > .mat-list-item-content | 
    self.driver.find_element(By.CSS_SELECTOR, ".mat-list-item:nth-child(2) > .mat-list-item-content").click()
    # 4 | click | css=div > .text-truncate:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, "div > .text-truncate:nth-child(1)").click()
    # 5 | click | css=.mat-list-item:nth-child(2) > .mat-list-item-content | 
    self.driver.find_element(By.CSS_SELECTOR, ".mat-list-item:nth-child(2) > .mat-list-item-content").click()
    # 6 | waitForElementPresent | css=.mat-body | 30000
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".mat-body")))
    # 7 | click | css=#mat-checkbox-2 .mat-checkbox-inner-container | 
    self.driver.find_element(By.CSS_SELECTOR, "#mat-checkbox-2 .mat-checkbox-inner-container").click()
    # 8 | click | css=#mat-checkbox-3 .mat-checkbox-inner-container | 
    self.driver.find_element(By.CSS_SELECTOR, "#mat-checkbox-3 .mat-checkbox-inner-container").click()
    # 9 | waitForElementPresent | css=.mat-body | 30000
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".mat-body")))
    # 10 | assertText | id=mat-input-0 | RESULTS
    assert self.driver.find_element(By.ID, "mat-input-0").text == "RESULTS"
  
