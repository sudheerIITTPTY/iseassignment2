from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#code for chrome opening
#setting path to chromedriver
chromeDriverPath = "chromedriver"

#github user credientials input
githubUsername = input("Enter username of github")
githubPassword = input("Enter password of github")

#driver to open chrome(web browser)
driver = webdriver.Chrome(chromeDriverPath)

#opening github login page in chrome using chrome driver
driver.get("https://github.com/login")


#accessing username and password in github login page by their id
username = driver.find_element_by_id("login_field")
password = driver.find_element_by_id("password")



#accessing login button by its name
signin = driver.find_element_by_name("commit")

#filling username and password field 
username.send_keys(githubUsername)
password.send_keys(githubPassword)

#clicking login or signing button
signin.click()

#incase new systems time to enter opt for login(30 sec waiting)
time.sleep(30)

#searching in github
search = driver.find_element_by_name("q")
search.send_keys("game engine")
search.send_keys(Keys.ENTER)

#printing top 5 result names
for vari in range(1,5):
    title = driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/ul/li["+str(vari)+"]/div[2]/div[1]/a")
    print(title.text)