
### List of contact names that match the contacts in your phone

listNames = ['tanmay','vivek','arjun']

### List of group names that are randomly chosen from
listGroups = ['group5', 'group6', 'group7', 'group9']


### Selenium automation
#- download http://chromedriver.storage.googleapis.com/index.html?path=2.21/
#- details https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import random


## Selenium web drivers
driver = None

def wait(web_opening_time=3):
	time.sleep(web_opening_time)

## load web driver for selenium : chrome
def web_driver_load():
	global driver
	driver = webdriver.Chrome(executable_path="C:\\Users\\PRAVESH\\Downloads\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")
## quit web driver for selenium
def web_driver_quit():
	driver.quit()
	quit()

## actual login in hockey app site
def whatsapp_login():
	
	driver.get('https://web.whatsapp.com/')
	time.sleep(30)
	#createGroup()
	
	for i in listGroups:
		time.sleep(5)
		try:
			createGroup(i)
		except NoSuchElementException:
			pass
		finally:
			print('Login Checked')






def createGroup(groupName):
	menu = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[4]/header/div[2]/div/span/div[4]/div/span')
	menu.click()
	time.sleep(2)
	new_grp = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[4]/header/div[2]/div/span/div[4]/span/div/ul/li[1]/div')
	new_grp.click()
	time.sleep(2)
	inp_name = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div/div[1]/div/div/div[2]/input')
	for i in listNames:
		inp_name.send_keys(i)
		user = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/span')
		user.click()
		time.sleep(2)
	add = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div/span/div/span')
	add.click()
	time.sleep(2)
	grp_name = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/p')
	grp_name.send_keys(groupName)
	clik = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/div[1]/span/div/span/div/div/span/div/div/span')
	clik.click()
	time.sleep(15)
	
	




### Main Method
if __name__ == "__main__":
	web_driver_load()
	whatsapp_login()
	print("Process complete successfully")
	web_driver_quit()