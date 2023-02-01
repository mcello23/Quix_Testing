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

class Test6AlphabeticalandRelevanceSelector():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_6AlphabeticalandRelevanceSelector(self):
    # Test name: 6-Alphabetical_and_Relevance_Selector
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
    # 7 | click | css=.fw-normal | 
    self.driver.find_element(By.CSS_SELECTOR, ".fw-normal").click()
    # 8 | click | css=.cdk-focused | 
    self.driver.find_element(By.CSS_SELECTOR, ".cdk-focused").click()
    # 9 | click | css=.fw-normal | 
    self.driver.find_element(By.CSS_SELECTOR, ".fw-normal").click()
    # 10 | click | css=.cdk-focused | 
    self.driver.find_element(By.CSS_SELECTOR, ".cdk-focused").click()
    # 11 | verifyText | css=.mat-button | Alphabetical
    # Assertion here is not totally correct, but just wanted to show that this selector isn't working
    assert self.driver.find_element(By.CSS_SELECTOR, ".mat-button").text == "Alphabetical"
  
