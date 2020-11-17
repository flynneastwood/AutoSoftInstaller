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


def dTube():
        
        global keyErrorElem

        wait = WebDriverWait(driver, 10)

        def dTube_upload():

            print("Logged In!")
            UploadBtnElem = wait.until(EC.visibility_of_element_located((By.XPATH,     #Get the "upload a video" button
                "/html/body/div/body/div[2]/div/nav[1]/a[3]"
                ))).click()
          
            
            
            srcElem = driver.find_element_by_xpath(                                         #Select from youtube link
                "/html/body/div[1]/body/div[5]/div/main/div/div/div[1]/div[2]/div/input"
                ).click()


            nextElem = driver.find_element_by_xpath(
                "/html/body/div[1]/body/div[5]/div/main/div/div/div[2]/button/div"          #Hit next button
                ).click()

            VideoLinkElem = driver.find_element_by_xpath(                                   #Get link to URL and paste in the youtube link
                "/html/body/div[1]/body/div[5]/div/main/div/div/div[1]/div/input"
                ).send_keys("a youtube url")

            

            pass

        def loginDtube():


            driver.get("https://d.tube/")

            driver.implicitly_wait(7) #Wait to load the page properly

            loginElem = wait.until(EC.visibility_of_element_located((By.XPATH,              #Find and click the login button
                "/html/body/div/body/div[1]/div[2]/div[3]/a/div"
                ))).click()
            avalonElem = wait.until(EC.visibility_of_element_located((By.XPATH,             #Select the Dtube authentification
                "/html/body/div/body/div[5]/div/main/div/div[3]"
                ))).click()
            driver.implicitly_wait(5)


            passwordElem = wait.until(EC.visibility_of_element_located((By.XPATH,           #Input password
                "/html/body/div/body/div[5]/div/main/div/div/form/div/div/div[2]/div/input"
                )))
            for character in (data['dtube']['password']):       #Used to slowdown typing, preventing blocks from bots.
                passwordElem.send_keys(character)


           
            usernameElem = wait.until(EC.visibility_of_element_located((By.XPATH,           #Input username
                "/html/body/div/body/div[5]/div/main/div/div/form/div/div/div[1]/div/input"
                ))).send_keys(data['dtube']['username'])



            submitElem = driver.find_element_by_xpath(                                      #Submit information
                "/html/body/div/body/div[5]/div/main/div/div/form/div/div/div[4]/button"
                )


            submitElem.submit()

        loginDtube()


        try:
            LoginSuccess = False
            keyErrorElem = wait.until(EC.visibility_of_element_located((By.XPATH,           #Check if login failed
                "/html/body/div[1]/body/div[6]/div/div[2]"
                )))
        except TimeoutException:
            dTube_upload()
            LoginSuccess = True


        #Loop the login process until access
        

        while LoginSuccess == False:    
            if keyErrorElem:
                print('Trying again')
                loginDtube()
                                                    
                
            else:
                     
                print("Success!")
                LoginSuccess = True
                
#driver.close()

