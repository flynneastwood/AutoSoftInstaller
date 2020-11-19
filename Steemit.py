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
steemitBody = (content['steemit']['body'])
tags = (content['steemit']['tags'])


videoUrl = 'https://www.youtube.com/'

thumbnail = '/home/tony/LazyPost/content/16_Forest.jpg'

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

		#Fill in the blog post. This order is the right way so far to 
		#input the post, otherwise, it all goes in the title for some reasons.
		
		blogTitle = wait.until(EC.visibility_of_element_located((By.XPATH, 
			"/html/body/div/div/div[3]/div/div[2]/form/div[1]/span/input"
			))).send_keys(title + " - Blender 3D")

		blogBody = wait.until(EC.visibility_of_element_located((By.XPATH, 
			"/html/body/div/div/div[3]/div/div[2]/form/div[2]/span/div/textarea"
			))).send_keys(body + "\nTimelapse of the whole thing below.\n\n\nNodes.\n\n" + steemitBody)
		blogTags = driver.find_element_by_xpath(                                       
			"/html/body/div/div/div[3]/div/div[2]/form/div[4]/span/span/input"         
			  ).send_keys(tags)

	   
		return True

steemit()

#driver.close()

