from selenium import webdriver
import time

print("Opening game")

zdriver = webdriver.Chrome()

gamelink = 'http://zzzscore.com/memory'

zdriver.get(gamelink)

load = 3.2 #Delay to load the game. Don't set it too low else the game will crash
time.sleep(load)


try:
    for i in range (2):
        cube = zdriver.find_element_by_css_selector("span.fa.fa-cube[style='display: none;']");
        cubeclick = cube.find_element_by_xpath("./..");
        cubeclick.click();

    for i in range (2):
        cubes = zdriver.find_element_by_css_selector("span.fa.fa-cubes[style='display: none;']");
        cubesclick = cubes.find_element_by_xpath("./..");
        cubesclick.click();
        
    for i in range (2):
        car = zdriver.find_element_by_css_selector("span.fa.fa-car[style='display: none;']");
        carclick = car.find_element_by_xpath("./..");
        carclick.click();


    for i in range (2):
        coffee = zdriver.find_element_by_css_selector("span.fa.fa-coffee[style='display: none;']");
        coffeeclick = coffee.find_element_by_xpath("./..");
        coffeeclick.click();

    for i in range (2):
        bomb = zdriver.find_element_by_css_selector("span.fa.fa-bomb[style='display: none;']");
        bombclick = bomb.find_element_by_xpath("./..");
        bombclick.click();

    for i in range (2):
        bolt = zdriver.find_element_by_css_selector("span.fa.fa-bolt[style='display: none;']");
        boltclick = bolt.find_element_by_xpath("./..");
        boltclick.click();

    for i in range (2):
        book = zdriver.find_element_by_css_selector("span.fa.fa-book[style='display: none;']");
        bookclick = book.find_element_by_xpath("./..");
        bookclick.click();

    for i in range (2):
        cake = zdriver.find_element_by_css_selector("span.fa.fa-birthday-cake[style='display: none;']");
        cakeclick = cake.find_element_by_xpath("./..");
        cakeclick.click();
        
    print("Game Over")

    
except:
    print("Error, script cannot run. Try again")
    print("If error persists, please decrease the value of 'load'")
    
