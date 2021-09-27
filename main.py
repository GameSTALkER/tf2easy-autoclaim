import os
import time
import colorama
from colorama import Fore, Style

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# CONFIG #

# SCRIPT #

options = webdriver.ChromeOptions()
	
options.add_argument("--disable-blink-features")
options.add_argument("--disable-infobars")
options.add_argument("--mute-audio")

options.add_argument(r"user-data-dir="+"C:/Users/GameSTALkER/AppData/Local/Google/Chrome/User Data/Profile 5")

browser = webdriver.Chrome(executable_path = './chromedriver.exe', options = options)

colorama.init()

kontinue = True
retry = False

for i_ in range(1337):
	browser.get('https://www.tf2easy.com/free')
	
	try:
		browser.find_element_by_xpath('//button[@class="free-button free-button-big free-skin"]').click()
		print(Fore.GREEN+'\nI\'am clicked reward button check your trade offers.\n'+Fore.RESET)
	except:
		print(Fore.RED+'\nLog in first before script can work.\n'+Fore.RESET)
		kk = input('\nType "OKAY" to continue: ')
		if str(kk).lower() == "okay":
			kontinue = True
			retry = True
		else:
			kontinue = False

	if retry == True:
		pass
	elif kontinue == True:
		time.sleep(43215)
	else:
		kk = input('\nType "OKAY" to continue: ')
		if kk.lower() == "okay":
			kontinue = True
			retry = True
		else:
			kontinue = False
