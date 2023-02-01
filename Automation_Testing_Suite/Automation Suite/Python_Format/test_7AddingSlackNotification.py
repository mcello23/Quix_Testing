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

class Test7AddingSlackNotification():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_7AddingSlackNotification(self):
    # Test name: 7-AddingSlackNotification
    # Step # | name | target | value
    # 1 | open |  | 
    self.driver.get("")
    # 2 | setWindowSize | 2044x1392 | 
    self.driver.set_window_size(2044, 1392)
    # 3 | click | css=div > .text-truncate:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, "div > .text-truncate:nth-child(1)").click()
    # 4 | click | css=.nodes > #threshold-alert-output_placeholder .mat-tooltip-trigger:nth-child(4) | 
    self.driver.find_element(By.CSS_SELECTOR, ".nodes > #threshold-alert-output_placeholder .mat-tooltip-trigger:nth-child(4)").click()
    # 5 | click | id=mat-input-0 | 
    self.driver.find_element(By.ID, "mat-input-0").click()
    # 6 | type | id=mat-input-0 | Slack
    self.driver.find_element(By.ID, "mat-input-0").send_keys("Slack")
    # 7 | waitForElementPresent | css=.mat-body | 30000
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".mat-body")))
    # 8 | click | css=.mat-card-content > div:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, ".mat-card-content > div:nth-child(1)").click()
    # 9 | click | css=.mt-1 > .mat-button-wrapper | 
    self.driver.find_element(By.CSS_SELECTOR, ".mt-1 > .mat-button-wrapper").click()
    # 10 | click | id=mat-input-3 | 
    self.driver.find_element(By.ID, "mat-input-3").click()
    # 11 | type | id=mat-input-3 |
    self.driver.find_element(By.ID, "mat-input-3").send_keys("")
    # 12 | click | css=.mat-button-wrapper span | 
    self.driver.find_element(By.CSS_SELECTOR, ".mat-button-wrapper span").click()
    # 13 | click | linkText=Workspace 1 | 
    # Not part of the scope, but wanted to automate this
    self.driver.find_element(By.LINK_TEXT, "Workspace 1").click()
  
