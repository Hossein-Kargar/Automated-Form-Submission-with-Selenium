"""
Author: Hossein Kargar
Date: 2025-01-09
Purpose: Automates form submission on the given webpage using Selenium WebDriver.

This script demonstrates the use of Selenium WebDriver to:
1. Launch a Chrome browser and navigate to a specified URL.
2. Interact with form fields such as email, subject, and message.
3. Submit the form and validate certain page elements to ensure proper functionality.
Requirements:
- Python 3.x
- Selenium Library
- ChromeDriver (compatible with your Chrome browser version)
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = 'https://hosseinkargar.pythonanywhere.com/contact.html'


def open_browser_and_navigate(url) :
    """
    Opens a Chrome browser instance and navigates to the specified URL.

    This function utilizes Selenium WebDriver to initiate a new Chrome browser,
    navigate to the URL provided as a parameter, and return the browser instance
    for further interaction or automation.

    :param url: The URL the browser should navigate to
    :type url: str
    :return: WebDriver instance representing the opened Chrome browser session
    :rtype: WebDriver
    """
    browser = webdriver.Chrome ( )
    browser.get ( url )
    return browser


def fill_form_fields(browser) :
    """
    Fills in the form fields on a webpage using the provided browser instance.
    This function interacts with the elements identified by their respective
    IDs and names, clears any pre-existing text, and inputs specified values.

    :param browser: A WebDriver instance used to interact with the web page.
    :type browser: WebDriver
    :return: None
    """
    email_field = browser.find_element ( By.ID , 'email' )
    email_field.clear ( )
    email_field.send_keys ( 'h@gmai.com' )

    subject_field = browser.find_element ( By.ID , 'subject' )
    subject_field.clear ( )
    subject_field.send_keys ( 'Testing' )

    message_field = browser.find_element ( By.NAME , 'message' )
    message_field.clear ( )
    message_field.send_keys ( 'Hi there, this is a test message' )


def submit_form(browser) :
    """
    Submits a form on a web page by interacting with a button element.

    :param browser: WebDriver instance used to interact with the web page.
    :type browser: WebDriver
    :return: None
    """
    submit_button = browser.find_element ( By.CLASS_NAME , 'btn-default' )
    submit_button.click ( )


# Main execution
browser = open_browser_and_navigate ( BASE_URL )

assert 'Contact me' in browser.page_source

fill_form_fields ( browser )
assert 'Send' in browser.page_source

submit_form ( browser )

time.sleep ( 10 )
browser.quit ( )
