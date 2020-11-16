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
options.binary_location = "/usr/bin/brave-browser"
driver_path = '/usr/bin/brave-browser'
driver = webdriver.Chrome('./chromedriver')

with open('ids.json', 'r') as json_file:     #get credentials from json
    data = json.load(json_file)

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
        "/html/body/m-app/m-page/m-body/div/div/m-newsfeed/div/div[1]/m-newsfeed--subscribed/m-composer/div/div"
        )

    postElem.click()

    postBody = driver.find_element_by_xpath(    
        "/html/body/m-app/m-page/m-overlay-modal/div/div[2]/m-composer__modal/m-composer__base/div/div/div/m-composer__textarea/div/m-text-input--autocomplete-container/textarea"
        )

    postBody.click()
    
    postBody.send_keys(title)

    postBody.send_keys(Keys.RETURN) #Jump a line in blog text

    postBody.send_keys(body)

    postBody.send_keys(Keys.RETURN) #Jump a line in blog text

    postBody.send_keys(tags)

    postBody.send_keys(Keys.RETURN)
        


    #driver.implicitly_wait(5)

    #Submit button
    #driver.find_element_by_xpath('/html/body/m-app/m-page/m-body/m-newsfeed/div[2]/div[2]/m-newsfeed--subscribed/minds-newsfeed-poster/div/div/form/div/button').click()

#driver.close()

minds()


