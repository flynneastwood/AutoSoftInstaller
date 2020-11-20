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
artstationBody = (content['artstation']['body'])
tags = (content['artstation']['tags'])

thumbnail = '/home/tony/LazyPost/content/16_Forest.jpg'

def artstation():

		driver.get("https://www.artstation.com")

		
		driver.implicitly_wait(7)                                                   #We find the login page and the text input.
		usernameElem = driver.find_element_by_xpath(
			"/html/body/div[1]/nav/ul/li[7]/a/span"
			).click()

		driver.implicitly_wait(7) #Wait to load the page                             #Username input.
		usernameElem = driver.find_element_by_xpath(
			"/html/body/div[1]/div[2]/div/div/div[2]/form/div[1]/input"
			).send_keys(data['artstation']['username'])
		
		passwordElem = driver.find_element_by_xpath(                                 #Password input.
			'/html/body/div[1]/div[2]/div/div/div[2]/form/div[2]/input'
			).send_keys(data['artstation']['password'], Keys.RETURN)


		# Finding upload new art button
		
		wait = WebDriverWait(driver, 20)

																						 
		postMenu = wait.until(EC.visibility_of_element_located((By.XPATH,             
			"/html/body/div[2]/nav/ul/li[4]/a"
			))).click() 

		postButton = wait.until(EC.visibility_of_element_located((By.XPATH,         
			"/html/body/div[2]/nav/ul/li[4]/ul/li[1]/a"
			))).click()                                                           
		   
		driver.implicitly_wait(5) 

		#Fill in the blog post. This order is the right way so far to 
		#input the post, otherwise, it all goes in the title for some reasons.
		
		blogTitle = wait.until(EC.visibility_of_element_located((By.XPATH, 
			"/html/body/div[4]/app-root/app-layout/ng-component/project-form/form/div/div[1]/div[1]/fieldset/form-input/div/input"
			))).send_keys(title + " - Blender 3D")

		uploadContent = wait.until(EC.visibility_of_element_located((By.XPATH, 
			"/html/body/div[4]/app-root/app-layout/ng-component/project-form/form/div/div[1]/project-assets-uploader/div[1]/div[1]/label[1]/i"
			))).send_keys(thumbnail)

		blogBody = wait.until(EC.visibility_of_element_located((By.XPATH, 
			"/html/body/div/div/div[3]/div/div[2]/form/div[2]/span/div/textarea"
			))).send_keys(body + "\nTimelapse of the whole thing below.\n\n\nNodes.\n\n" + steemitBody)

		blogTags = driver.find_element_by_xpath(                                       
			"/html/body/div/div/div[3]/div/div[2]/form/div[4]/span/span/input"         
			  ).send_keys(tags)

	   
		return True

artstation()

#driver.close()

