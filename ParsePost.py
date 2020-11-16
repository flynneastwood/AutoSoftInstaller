import os
from bs4 import BeautifulSoup

post = open("Post.html", "r") # Path to HTML file used to get post title, body text and hashtags.

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

def getVideoDesc():
	videoDesc = str(soup.p).strip("</p>")
	return videoDesc


