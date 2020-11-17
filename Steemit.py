import json
import pyautogui
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from ParsePost import getTitle, getBody, getHashtags, getVideoDesc


driver = webdriver.Chrome('./chromedriver')

with open('ids.json', 'r') as json_file:     #get credentials from json
    data = json.load(json_file)

#Pour utiliser Brave.
#driver = webdriver.Chrome(executable_path ='C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe')
title = getTitle()
body = getBody()
tags = getHashtags()
videoDesc = getVideoDesc()

videoUrl = 'https://www.youtube.com/'

thumbnail = './thumbnail.jpg'

def steemit():

        driver.get("https://www.steemit.com/")

        
        driver.implicitly_wait(7)                                                   #We find the login page and the text input.
        usernameElem = driver.find_element_by_xpath(
            "//*[@id='content']/div/div[2]/div/div/header/nav/div[3]/span[1]/a[1]"
            ).send_keys(Keys.RETURN)

        driver.implicitly_wait(7) #Wait to load the page                             #Username input.
        usernameElem = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/form/div[1]/input"
            ).send_keys(data['steemit']['username'])
        
        passwordElem = driver.find_element_by_xpath(                                 #Password input.
            '/html/body/div[2]/div/div[2]/div/div/form/div[2]/input'
            ).send_keys(data['steemit']['password'], Keys.RETURN)


        # Get write blog icon and fills each fields using the HTML file.
        
        wait = WebDriverWait(driver, 20)

                                                                                         
        writePost = wait.until(EC.visibility_of_element_located((By.XPATH,             # wait for the button to be available
            "/html/body/div/div/div[2]/div/div/header/nav/div[3]/a"
            )))

        writePost.click()                                                              #click the write blog button
           
        driver.implicitly_wait(5) 

        blogTags = driver.find_element_by_xpath(                                       #Fill in the blog post. This order is the right way so far to 
            "/html/body/div/div/div[3]/div/div[2]/form/div[4]/span/span/input"         #input the post, otherwise, it all goes in the title for some reasons.
            ).send_keys(tags)
        blogTitle = wait.until(EC.visibility_of_element_located((By.XPATH, 
            "/html/body/div/div/div[3]/div/div[2]/form/div[1]/span/input"
            ))).send_keys(title)
        blogBody = wait.until(EC.visibility_of_element_located((By.XPATH, 
            "/html/body/div/div/div[3]/div/div[2]/form/div[2]/span/div/textarea"
            ))).send_keys(body)

       
        return True

steemit()

#driver.close()

