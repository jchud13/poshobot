from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

login = {
	'login': 'click',
	'textbox-username': 'junklybot',
	'textbox-password': 'damage',
	'login': 'click'}

driver = webdriver.Firefox()
driver.get('https://play.pokemonshowdown.com')
time.sleep(5)
button = driver.find_element_by_name("login")
button.click()

username = driver.find_element_by_name("username")
username.send_keys("teesterbot")

chooseName = driver.find_element_by_css_selector("button[type='submit']")
chooseName.click()

password = driver.find_element_by_name("password")
password.send_keys("thisispass")

passwordClick = driver.find_element_by_xpath('//*[@type="submit"]')
passwordClick.click()