from selenium import webdriver
import time

zdriver = webdriver.Chrome()

#Constants
gamelink = 'http://zzzscore.com/1to50/en/'

print("Opening game")
zdriver.get(gamelink)

time.sleep(5) #Delay to load the website. You can change it

print("Clicking 1 to 50")
for x in range(99,49,-1):
    zdriver.find_element_by_css_selector("[style='z-index:%d']" %x).click();
    #time.sleep(0.5) #Time delay in case you want a slower result, change 0.5 to required delay between clicks (in seconds)
