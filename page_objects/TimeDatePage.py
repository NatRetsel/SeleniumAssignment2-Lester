"""
    This module contains locators and getter methods for each locators in the timeanddate page
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class TimeDatePage:
    # Class Variables - website and locators
    time_and_date_site: str = "https://www.timeanddate.com/worldclock/singapore/singapore"
    link_fullscreen = (By.CSS_SELECTOR, "#full-clk")
    
    exit_fullscreen_link = (By.LINK_TEXT, "Exit")
    
    def __init__(self, driver:WebDriver):
        self.driver = driver
    
    # Getter methods
    def get_time_and_date_site(self) -> None:
        # Navigate to timeanddate
        self.driver.get(TimeDatePage.time_and_date_site)
    
    def get_link_fullscreen(self) -> WebElement:
        # Locate and return fullscreen linktext webelement
        return self.driver.find_element(*TimeDatePage.link_fullscreen)