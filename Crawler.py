#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initiate browser instance
def Driver():
    global driver
    chromedriver_path = '/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    return driver

driver_obj = Driver()

def login_facebook():
    username='rockwithsoumya@gmail.com'
    password='soumya@8017284515'
    driver_obj.get('https://www.facebook.com')
    print(">>>Facebook URL triggered")
    driver_obj.implicitly_wait(5)
    driver_obj.maximize_window()
    driver_obj.find_element(By.ID,"email").send_keys(username)
    print("\n>>>Entered email")
    driver_obj.find_element(By.ID,"pass").send_keys(password)
    print("\n>>>Entered password")
    driver_obj.find_element(By.ID,"u_0_q").click()
    print("\n>>>Clicked on the login button")
    page_title = driver_obj.title
    print("\n>>>The title of the page is: "+page_title)

def goto_profile_Section():
    driver_obj.find_element(By.XPATH,"//a[@title='Profile']").click()
    driver_obj.find_element(By.XPATH,"//a[@data-tab-key='friends']").click()

def scrape_friend_facebook():
    list_friends = driver_obj.find_elements(By.XPATH,"")

def tear_browser():
    driver_obj.quit()

login_facebook()
goto_profile_Section()
tear_browser()