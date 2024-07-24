from fpdf import FPDF
import csv
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import string
import time
import instaloader
import tkinter as tk
from tkinter import ttk

def profile_detail():
    print("profile_detail")
    
    email = email_entry.get()
    password = password_entry.get()
    target = target_entry.get()
    
    options = webdriver.ChromeOptions()
    driver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    driver.maximize_window()
    # increase_progress(10)
    url = 'https://www.facebook.com/'
    driver.get(url)
    # increase_progress(20)
    # Check if a session file exists
    try:
        with open('fb_session.pickle', 'rb') as file:
            session_data = pickle.load(file)
            email = session_data['email']
            password = session_data['password']
    except FileNotFoundError:
        # No session file found, enter login credentials
        # email = input("Enter your email: ")
        # password = input("Enter your password: ")
        # Save login credentials to a session file
        session_data = {'email': email, 'password': password}
        with open('fb_session.pickle', 'wb') as file:
            pickle.dump(session_data, file)

    user_name = driver.find_element(By.ID, 'email')
    user_name.send_keys(email)
    sleep(1)
    # increase_progress(30)
    password_element = driver.find_element(By.ID, 'pass')
    password_element.send_keys(password)
    sleep(1)

    login_btn = driver.find_element(By.NAME, 'login')
    login_btn.click()
    # increase_progress(50)
    sleep(7)
    driver.get(target)
    #https://www.facebook.com/DR.HAJARIRAM
    
    ############################# user INTO working properly ################################
    intro = driver.find_element(By.CSS_SELECTOR,'span.x193iq5w.xeuugli.x13faqbe.x1vvkbs.x10flsy6.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x4zkp8e.x41vudc.x6prxxf.xvq8zen.xo1l8bm.xzsf02u')
    intro_text = intro.text
    print(intro_text)
    print("========================================================")
    sleep(2)
    # increase_progress(60)
    # ############################## user profile text working ###########################################

    profile = driver.find_elements(By.CSS_SELECTOR,'span.x193iq5w.xeuugli.x13faqbe.x1vvkbs.x10flsy6.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x4zkp8e.x41vudc.x6prxxf.xvq8zen.xo1l8bm.xzsf02u.x1yc453h')
    for i in profile:
        profile_text = i.text
        print(profile_text)
    print("========================================================")
    # increase_progress(70)
    # sleep(2)

    ########################### user about us text ######################################################

    driver.get(target+"/about")
    sleep(5)
    ###### overview done
    main_class_elements = driver.find_elements(By.CLASS_NAME, "x193iq5w")

    for element in main_class_elements:
        n = element.text.strip()
        print(n)
    print("========================================================")

    # increase_progress(80)
    ####### 
    driver.get(target+"/about_details")
    sleep(4)

    # Find all elements with the specified class name
    overview_1 = driver.find_elements(By.CLASS_NAME, "x1gan7if")
    for data in overview_1:
        m = data.text
        print(m)
    print("========================================================")
    file_path = f"output/user_profile_report.csv"
    try:
        with open(file_path, 'w') as f:
            f.write(intro_text)
            f.write(profile_text)
            f.write(m)
            f.write(n)
        print(f"File '{file_path}' created successfully.")
    except Exception as e:
        print(f"An error occurred while writing the file: {e}")