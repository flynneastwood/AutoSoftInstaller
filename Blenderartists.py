import json
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome('./chromedriver')

with open('ids.json', 'r') as json_file:     #get credentials from json
	data = json.load(json_file)
with open('postContent.json', 'r') as json_file:     #get post content
	content = json.load(json_file)

title = (content['GENERAL']['title'])
body = (content['GENERAL']['body'])
blenderartistsBody = (content['blenderartists']['body'])
tags = (content['blenderartists']['tags'])

thumbnail = '/home/tony/LazyPost/content/16_Forest.jpg'

def blenderartists():

		driver.get("https://blenderartists.org")

		
		driver.implicitly_wait(7)                                                   #We find the login page and the text input.
		usernameElem = driver.find_element_by_xpath(
			"/html/body/section/div/div[1]/header/div/div/div[2]/span/button[2]"
			).click()

		driver.implicitly_wait(7) #Wait to load the page                             #Username input.
		usernameElem = driver.find_element_by_xpath(
			"/html/body/section/div/div[4]/div/div/div/div[3]/div[1]/form/div[1]/table/tbody/tr[1]/td[2]/input"
			).send_keys(data['blenderartists']['username'])
		
		passwordElem = driver.find_element_by_xpath(                                 #Password input.
			'/html/body/section/div/div[4]/div/div/div/div[3]/div[1]/form/div[1]/table/tbody/tr[2]/td[2]/input'
			).send_keys(data['blenderartists']['password'], Keys.RETURN)


		# Finding upload new art button
		
		wait = WebDriverWait(driver, 20)

		

		FinishedArtworks = wait.until(EC.visibility_of_element_located((By.XPATH,             
			"/html/body/section/div/div[2]/div[5]/div[2]/div/div/div/div/div[1]/table/tbody/tr[1]/td[1]/div/span[1]/a/span[2]"
			))).click() 


		clickNewTopic = wait.until(EC.visibility_of_element_located((By.XPATH,             
			"/html/body/section/div/div[2]/div[3]/div/section/button/span"
			))).click()                                                          
		   
		driver.implicitly_wait(5) 

		#Fill in the blog post. This order is the right way so far to 
		#input the post, otherwise, it all goes in the title for some reasons.
		
		blogTitle = wait.until(EC.visibility_of_element_located((By.XPATH, 
			"/html/body/section/div/div[6]/div[3]/div[1]/div[2]/div[1]/input"
			))).send_keys(title + " - Blender 3D")

		#uploadContent = wait.until(EC.visibility_of_element_located((By.XPATH, 
			#"/html/body/div[4]/app-root/app-layout/ng-component/project-form/form/div/div[1]/project-assets-uploader/div[1]/div[1]/label[1]"
			#))).send_keys(thumbnail)

		blogBody = wait.until(EC.visibility_of_element_located((By.XPATH, 
			"/html/body/div[4]/app-root/app-layout/ng-component/project-form/form/div/div[1]/div[2]/fieldset/form-text/div/textarea"
			))).send_keys(artstationBody + body)

		checkMedium = wait.until(EC.visibility_of_element_located((By.XPATH, 
			"/html/body/div[4]/app-root/app-layout/ng-component/project-form/form/div/div[1]/div[3]/fieldset/project-medium/div/div[1]/div[2]/label/span[2]"
			))).click()

		#softwaresSelect = wait.until(EC.visibility_of_element_located((By.XPATH, 
		#	"/html/body/div[4]/app-root/app-layout/ng-component/project-form/form/div/div[1]/div[3]/fieldset/project-software/div/software-select/span/span[1]/span/span[1]/span"
		#	))).click()

		#softwaresInput = wait.until(EC.visibility_of_element_located((By.XPATH, 
		#	"/html/body/span/span/span[1]/input"
		#	))).send_keys("Blender")
		#softwaresSelect = wait.until(EC.visibility_of_element_located((By.XPATH, 
		#	"/html/body/span/span/span[1]"
		#	))).click()

		blogTags = driver.find_element_by_xpath(                                       
			"/html/body/div[4]/app-root/app-layout/ng-component/project-form/form/div/div[1]/div[3]/fieldset/div[5]/div/a"         
			  ).click()

	   
		return True

blenderartists()

#driver.close()

