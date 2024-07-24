from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import time
import os
import requests
from bs4 import BeautifulSoup as bs
import tkinter as tk

root = tk.Tk()
root.title("AMAZON_SCRAPING")
root.geometry('400x300')

label = tk.Label(root, text="HELLO!!!!!!!!")
label.pack()
label1 = tk.Label(root, text="WHAT YOU WOULD LIKE TO SCRAP?????")
label1.pack()

def grocery_details():
    print("GROCERY DETAILS")

    options = webdriver.ChromeOptions()
 
    driver_path = ChromeDriverManager().install()

    # Create the Chrome driver instance
    driver = webdriver.Chrome(executable_path=driver_path, options=options)

    # driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url=driver.get('https://www.amazon.in/')
    sleep(2)
    driver.maximize_window()

    # find_friends=driver.find_element(By.CLASS_NAME,'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f')
    # find_friends.click()

    select_cate=driver.find_element(By.ID,'twotabsearchtextbox')
    select_cate.send_keys('grocery items',Keys.ENTER)
    sleep(2)

    kellogs=driver.find_elements(By.CLASS_NAME,'a-size-base-plus')
    price=driver.find_elements(By.CLASS_NAME,'a-price-whole')

    with open('grocery_product_detail.csv','w') as file:
        for i,j in zip(kellogs,price):

            file.write('product name: '+i.text+'\n')
            file.write('product price: '+j.text+'\n'+'\n')

            print('product name: ',i.text)
            print("product price: ",j.text)
            print("   ")
            print("   ")

    driver.quit()

def food_details():
    print("FOOD DETAILS")  
        
    options = webdriver.ChromeOptions()

    driver_path = ChromeDriverManager().install()
    
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url=driver.get('https://www.amazon.in/')
    sleep(2)
    driver.maximize_window()
    
    # find_friends=driver.find_element(By.CLASS_NAME,'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f')
    # find_friends.click()
    
    select_cate=driver.find_element(By.ID,'twotabsearchtextbox')
    select_cate.send_keys('restaurant',Keys.ENTER)
    sleep(2)
    
    restro=driver.find_elements(By.CLASS_NAME,'a-size-base-plus')
    price=driver.find_elements(By.CLASS_NAME,'a-price-whole')
    
    with open('restro_product_detail.csv','w') as file:
        for i,j in zip(restro,price):
            
            file.write('product name: '+i.text+'\n')
            file.write('product price: '+j.text+'\n'+'\n')
            
            print('product name: ',i.text)
            print("product price: ",j.text)
            print("   ")
            print("   ")
    
    driver.quit() 

def fashion_details():
    print("FASHION DETAILS")

    options = webdriver.ChromeOptions()
  
    driver_path = ChromeDriverManager().install()

    # Create the Chrome driver instance
    driver = webdriver.Chrome(executable_path=driver_path, options=options)

    # driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url=driver.get('https://www.amazon.in/')
    sleep(2)
    driver.maximize_window()

    select_cate=driver.find_element(By.ID,'twotabsearchtextbox')
    select_cate.send_keys('fashion',Keys.ENTER)
    sleep(2)

    fashion=driver.find_elements(By.CLASS_NAME,'a-size-base-plus')
    price=driver.find_elements(By.CLASS_NAME,'a-price-whole')

    with open('fashion_product_detail.csv','w') as file:
        for i,j in zip(fashion,price):

            file.write('product name: '+i.text+'\n')
            file.write('product price: '+j.text+'\n'+'\n')

            print('product name: ',i.text)
            print("product price: ",j.text)
            print("   ")
            print("   ")

    driver.quit()

grocery_button = tk.Button(root, text="Grocery Item",command=grocery_details)
grocery_button.pack()
grocery_button.place(x=150,y=90)

food_button = tk.Button(root, text="Food Item",command=food_details)
food_button.pack()
food_button.place(x=160,y=140)

fashion_button = tk.Button(root, text="Fashion Item",command=fashion_details)
fashion_button.pack()
fashion_button.place(x=150,y=190)

root.mainloop()