import json
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from ParsePost import getTitle, getBody, getHashtags, getVideoDesc


options = webdriver.ChromeOptions()
options.binary_location = "/opt/brave.com/brave-browser"
#driver_path = '/home/tony/LazyPost/chromedriver'
driver = webdriver.Chrome('./chromedriver')

with open('ids.json', 'r') as json_file:     #get credentials from json
    data = json.load(json_file)

#Pour utiliser Brave.
#driver = webdriver.Chrome(executable_path ='/opt/brave.com/brave/brave-browser')
title = getTitle()
body = getBody()
tags = getHashtags()
videoDesc = getVideoDesc()

thumbnail = './thumbnail.jpg'

def minds():

    driver.get("https://www.minds.com/")

    #We find the login page and the text input.
    usernameElem = driver.find_element_by_link_text('Login').click()
    
    #Credentials input.
    usernameElem = driver.find_element_by_id('username').send_keys((data['minds']['username']))
    passwordElem = driver.find_element_by_id('password').send_keys((data['minds']['password'], Keys.RETURN))
        

    driver.implicitly_wait(7) #Wait to load the page properly


    # Get text box and add post.txt
    postElem = driver.find_element_by_xpath(    
        '/html/body/m-app/m-page/m-body/m-newsfeed'
        '/div[2]/div[2]/m-newsfeed--subscribed/minds-newsfeed-poster'
         '/div/div/form/m-text-input--autocomplete-container/textarea'
        )

    postElem.send_keys(title)

    postElem.send_keys(Keys.RETURN) #Jump a line in blog text

    postElem.send_keys(body)

    postElem.send_keys(Keys.RETURN) #Jump a line in blog text

    postElem.send_keys(tags)

    postElem.send_keys(Keys.RETURN)
        


    driver.implicitly_wait(5)

    #Submit button
    #driver.find_element_by_xpath('/html/body/m-app/m-page/m-body/m-newsfeed/div[2]/div[2]/m-newsfeed--subscribed/minds-newsfeed-poster/div/div/form/div/button').click()

driver.close()


