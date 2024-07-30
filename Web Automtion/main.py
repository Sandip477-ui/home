from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://www.google.com/')
box = browser.find_element(by=By.NAME,value="q")
box.send_keys("technologychnnel"+Keys.RETURN)