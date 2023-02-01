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

class Test4DeploymentStuck():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_4DeploymentStuck(self):
    # Test name: 4-DeploymentStuck
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
    # 6 | click | id=mat-input-0 | 
    self.driver.find_element(By.ID, "mat-input-0").click()
    # 7 | type | id=mat-input-0 | Demo Data
    self.driver.find_element(By.ID, "mat-input-0").send_keys("Demo Data")
    # 8 | waitForElementPresent | css=.mat-body | 30000
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".mat-body")))
    # 9 | click | css=.mat-card-content > div:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, ".mat-card-content > div:nth-child(1)").click()
    # 10 | click | css=.mt-1 | 
    self.driver.find_element(By.CSS_SELECTOR, ".mt-1").click()
    # 11 | click | css=.mat-button-wrapper span | 
    self.driver.find_element(By.CSS_SELECTOR, ".mat-button-wrapper span").click()
    # 12 | assertText | css=.mat-h1 | Workspace 1
    assert self.driver.find_element(By.CSS_SELECTOR, ".mat-h1").text == "Workspace 1"
  
