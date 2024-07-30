from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get("https://technologychannel.github.io/SampleWebsite/register.html")
username = browser.find_element(by=By.NAME,value="username")
username.send_keys("sandipkerung02@gmail.com")
password = browser.find_element(by=By.NAME,value="password")
password.send_keys("7654321")
time.sleep(3)
button = browser.find_element(by=By.TAG_NAME("button"))
button.click()
