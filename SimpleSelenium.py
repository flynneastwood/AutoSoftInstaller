from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('./chromedriver')
driver.get("https://krita.org/fr/telechargement/krita-desktop/")

elem = driver.find_element_by_id('sixty-four-bit-windows-installer').click()


print(elem)

#driver.close()
