from selenium import webdriver
import time

print("Opening game")

zdriver = webdriver.Chrome()

gamelink = 'http://zzzscore.com/color2/'

zdriver.get(gamelink)

time.sleep(5)#Delay to load the website. You can change it
for x in range(1, 10000):
    try:
        zdriver.find_element_by_css_selector("div.main").click();
        #time.sleep(1) #Time delay between clicks
    except:
        print("Game Over")
        break 
        
