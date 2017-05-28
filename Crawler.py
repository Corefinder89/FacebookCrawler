#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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
    print("\n>>>In the profile section")
    driver_obj.find_element(By.XPATH,"//a[@data-tab-key='friends']").click()
    print("\n>>>In the friend's section")

def scrape_friend_facebook():
    SCROLL_PAUSE_TIME=5
    last_scroll_height = driver_obj.execute_script("return document.body.scrollTop")
    while True:
        driver.execute_script("window.scrollBy(0,1000)","")
        new_scroll_height = driver.execute_script("return document.body.scrollTop")
        time.sleep(SCROLL_PAUSE_TIME)
        list_friends = driver_obj.find_elements(By.XPATH,"//div[@class='uiProfileBlockContent']//a")
        print("\n>>>Fetching objects")
        if new_scroll_height==last_scroll_height:
            break
        last_pixel_height=new_scroll_height

def tear_browser():
    driver_obj.quit()

login_facebook()
goto_profile_Section()
scrape_friend_facebook()
tear_browser()
