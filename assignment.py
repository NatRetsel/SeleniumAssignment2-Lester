"""
    Selenium Assignment - Automated Navigation Using Selenium
    
    Objective:
        - Automating the following instructions that takes screenshot of the current Singapore time displayed
        on Google search and timeanddate.com
            - Navigate to google.com.sg with any browser, I'll be using Chrome
            - Input "Singapore Time" in the search bar, press enter (Key input)
            - Take screenshot
            - Press back
            - Navigate to www.timeanddate.com/worldclock/singapore/singapore
            - Click on Full Screen link text below the clock
            - Take screenshot when it is full screen
            - Quit Browser.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from page_objects.GooglePage import GooglePage
from page_objects.TimeDatePage import TimeDatePage
import time


class SeleniumAssignment:
    """
        This class contains class variables and methods related to the assignment.
        Class variables:
            - filenames of screenshots
            - google search string
        
        Methods
            - Constructor intializes the webdriver object for Chrome
            - a helper method that takes screenshot and saves to the given filename parameter
            - do entire assignment
                - Initializes the page objects for both google home page and timeanddate page from page_objects library
                - Gets the home pages of both sites using their respective getter methods
                - Locates respective elements using locators stored as class variables
                - I've included the explicit wait option as a boolean so the google search screenshot looks proper
                    - Looks like time.sleep() is required if we want to take a nice screenshot of fullscreen clock
                    in timeanddate
    """
    
    # Class Variables - website, search string
    screenshot_filename_google: str = "GoogleSearchSingaporeTime.png"
    screenshot_filename_timedate: str = "timeanddateSingapore.png"
    
    search_string: str = "Singapore Time"
    
    # Constructor initializes webdriver
    def __init__(self):
        self.driver: WebDriver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    # Take screenshot method
    def take_screenshot(self, filename: str):
        self.driver.save_screenshot(filename)
    
    # Do entire assignment
    def do_assignment(self, explicit_wait: bool = False):
        
        
        # Instantiate GooglePage object and get google site
        GoogleHomePage: GooglePage = GooglePage(self.driver)
        GoogleHomePage.get_google()
        
        # Locate search bar, input search string and press enter
        search_bar: WebElement = GoogleHomePage.get_search_bar()
        search_bar.send_keys(SeleniumAssignment.search_string)
        search_bar.send_keys(Keys.ENTER)
        
        # If explcit wait is enabled, this will wait for expected condition before proceeding
        if explicit_wait:
            wait: WebDriverWait = WebDriverWait(self.driver, 5)
            wait.until(expected_conditions.visibility_of_element_located(GooglePage.time_in_singapore))
        
        # Takes and save screenshot
        self.take_screenshot(SeleniumAssignment.screenshot_filename_google)
        
        # Press back
        self.driver.back()
        
        # Navigate to timeanddate page by first instantiating TimeDatePage object
        TimeDateHomePage: TimeDatePage = TimeDatePage(self.driver)
        TimeDateHomePage.get_time_and_date_site()
        
        # Locate fullscreen link text and click it
        TimeDateHomePage.get_link_fullscreen().click()
        
        # If explcit wait is enabled, this will wait for expected condition before proceeding
        if explicit_wait:
            wait: WebDriverWait = WebDriverWait(self.driver, 5)
            wait.until(expected_conditions.element_to_be_clickable(TimeDatePage.exit_fullscreen_link))
            
        # Save screenshot
        self.take_screenshot(SeleniumAssignment.screenshot_filename_timedate)
        
        # Close driver
        self.driver.close()


if __name__ == "__main__":
    assignment: SeleniumAssignment = SeleniumAssignment()
    assignment.do_assignment()
    
    # Uncomment line below to run assigment with explicit wait -> saves a nice screenshot of google search
    # assignment.do_assignment(explicit_wait=True)        

