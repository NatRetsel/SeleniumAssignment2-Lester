"""
    This module contains locators and getter methods for each locators in the google page
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class GooglePage:
    # Class Variables - website and locators
    google_site: str = "https://www.google.com.sg"
    search_bar: tuple = (By.XPATH, "//textarea[@name='q']")
    
    time_in_singapore: tuple = (By.XPATH, "//body/div[@id='main']/div[@id='cnt']/div[@id='rcnt']/div[@id='center_col']/div[@id='res']/div[@id='search']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]")
    
    def __init__(self, driver:WebDriver):
        self.driver = driver
    
    # Getter methods
    def get_google(self) -> None:
        # Navigate to google.com.sg
        self.driver.get(GooglePage.google_site)
    
    def get_search_bar(self) -> WebElement:
        # Locate and return search bar webelement
        return self.driver.find_element(*GooglePage.search_bar)