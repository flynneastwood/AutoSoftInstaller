import os
from bs4 import BeautifulSoup

post = open("Post.html", "r")  

soup = BeautifulSoup(post, 'html.parser')

def getTitle():
	title = str(soup.title).strip("</title>")
	return title

def getBody():
	body = str(soup.body).strip("</body>")
	return body

def getHashtags():
	#Get the text in HTML and split words into a list.
	textLine = str(soup.h1).strip("</h1>")   
	hashtags = list(textLine.split())

	return hashtags

getHashtags()