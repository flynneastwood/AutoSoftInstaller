import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from ParsePost import getTitle, getBody, getHashtags, getVideoDesc
from YoutubeUploader import main


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

videoMediaList =[]
videoPath = open('./testVidUpload.mp4', 'rb')

videoMediaList.append(str(videoPath))

thumbnail = './thumbnail.jpg'

def main():


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

    def lbry():
        pass

    def youtube():
        pass



    bitchute()
    

    #driver.close()
if __name__== "__main__":
  main()

