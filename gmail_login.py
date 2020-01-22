"""
This program will take your gmail username and password as input and print recent
top 50 sender name(not email id just names)

"""



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#code for chrome opening
#setting path to chromedriver
chromeDriverPath = "chromedriver"

#taking input from user(email and password) 
mail =  input("Enter your gmail email")
passwd = input("Enter your gmail password")

#driver to open chrome(web browser)
driver = webdriver.Chrome(chromeDriverPath)
driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

#finding email id
email = driver.find_element_by_id("identifierId")
#filling email id
email.send_keys(mail)
#finding nextbutton  using it id
nextButton = driver.find_element_by_id("identifierNext")
#clicking next button to goto next page
nextButton.click()

#waiting time for program to go to next page
time.sleep(5)

#finding password input form using it's id
password = driver.find_element_by_name("password")
#filling input password in the box
password.send_keys(passwd)
#finding signing button using it's id
passwordNext = driver.find_element_by_id("passwordNext")
#clicking signing buttion
passwordNext.click()

#loading time for mail
time.sleep(10)

#opening recent50sender.txt
file = open("recent50sender.txt","w")

#reading first 50 (recent) sender names using xpath selenium component
for i in range(1,50,1):
	#sender_xpath creating
	sender_xpath="/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[3]/div[2]/div/table/tbody/tr["+ str(i) +"]/td[5]/div[2]/span/span"
	#finding sender name
	sender=driver.find_element_by_xpath(sender_xpath).text
	#writting sender to file
	file.write(sender+'\n')
#closing file
file.close()