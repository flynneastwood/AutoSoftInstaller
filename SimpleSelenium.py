from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

#Pour utiliser Brave.
#driver = webdriver.Chrome(executable_path ='C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe')


def main():


    def readPost():
        #Reads the blog file and store it in a variable
        f = open('post.txt', 'r')
        if f.mode == 'r':
            contents = f.read()
        return contents

    def minds():
        contents = readPost()
        image = open("imgs/Image01.png", "r")

        driver.get("https://www.minds.com/")

        #We find the login page and the text input.

        usernameElem = driver.find_element_by_link_text('Login').click()
        usernameElem = driver.find_element_by_id('username')
        username = input('What is your username?')
        usernameElem.send_keys(username)

        #Password input.

        passwordElem = driver.find_element_by_id('password')
        password = input('What is your password?')
        passwordElem.send_keys(password, Keys.RETURN)

        driver.implicitly_wait(7) #Wait to load the page properly

        # Get text box and add post.txt
        postElem = driver.find_element_by_xpath(
            '/html/body/m-app/m-page/m-body/m-newsfeed'
            '/div[2]/div[2]/m-newsfeed--subscribed/minds-newsfeed-poster'
            '/div/div/form/m-text-input--autocomplete-container/textarea'
            )
        postElem.send_keys(contents)

        #Submit button
        driver.implicitly_wait(5)
        #driver.find_element_by_xpath('/html/body/m-app/m-page/m-body/m-newsfeed/div[2]/div[2]/m-newsfeed--subscribed/minds-newsfeed-poster/div/div/form/div/button').click()

    def steemit():
        pass

    def dTube():
        pass

    def bitchute():
        pass

    def lbry():
        pass

    def youtube():
        pass



    minds()
    #driver.close()
if __name__== "__main__":
  main()

