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


videoMediaList =[]
videoPath = open('./testVidUpload.mp4', 'rb')

videoMediaList.append(str(videoPath))

thumbnail = './thumbnail.jpg'

def bitchute():
    def loginBitchute():
        driver.get("https://www.bitchute.com/")

        wait = WebDriverWait(driver, 10)

        driver.implicitly_wait(7) #Wait to load the page properly

        loginElem = wait.until(EC.visibility_of_element_located((By.XPATH,              #Find and click the login button
            "/html/body/nav/div[1]/div[2]/div[4]/span/a[1]"
            ))).click()

        usernameElem = wait.until(EC.visibility_of_element_located((By.XPATH,           #Input username
            "/html/body/div[1]/div/div/div[2]/div/div[1]/form/div[2]/input"
            ))).send_keys(data['bitchute']['username'])

        passwordElem = wait.until(EC.visibility_of_element_located((By.XPATH,           #Input username
            "/html/body/div[1]/div/div/div[2]/div/div[1]/form/div[3]/input"
            ))).send_keys(data['bitchute']['password'])

        submitElem = driver.find_element_by_xpath(                                      #Submit information
            "/html/body/div[1]/div/div/div[3]/button[1]"
            ).click()


        def uploadBitchute():

            print("Logged In!")

            wait = WebDriverWait(driver, 10)

            try:

                UploadBtnElem = wait.until(EC.visibility_of_element_located((By.XPATH,     #Get the "upload a video" button
                "/html/body/nav/div[1]/div[2]/div[4]/a"
                    ))).click()

            except TimeoutException:
                print('Not found')

            videoTitleElem = driver.find_element_by_xpath(                                       
            "/html/body/div/div/div/form/div[1]/textarea"         
            ).send_keys(title)

            videoDescElem = wait.until(EC.visibility_of_element_located((By.XPATH, 
            "/html/body/div/div/div/form/div[2]/textarea"
            ))).send_keys(videoDesc)

            uploadVideoElem = wait.until(EC.visibility_of_element_located((By.ID, 
            "video_upload"
            ))).send_keys("C:/Users/Tony Laptop/Documents/GitHub/LazyPost/testVidUpload.mp4")

            uploadThumbnailElem = wait.until(EC.visibility_of_element_located((By.ID, 
            "cover_upload"
            ))).send_keys("C:/Users/Tony Laptop/Documents/GitHub/LazyPost/thumbnail.jpg")

        loginBitchute()
        uploadBitchute()

bitchute()
    #driver.close()

