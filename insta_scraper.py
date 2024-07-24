from fpdf import FPDF
import os
import csv
import sys
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QApplication, QProgressBar, QPushButton, QVBoxLayout, QWidget,QLabel,QMessageBox
import time
import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import glob
import lzma
from subprocess import call
import instaloader
import tkinter as tk
from tkinter import ttk

def profile_button_clicked():
    email = email_entry.get()
    password = password_entry.get()
    target = target_entry.get()
    print(email)
    print(password)
    print(target)
    # Perform profile-related operations with the email, password, and target

def profile_detail():
    try:
        email = email_entry.get()
        password = password_entry.get()
        target = target_entry.get()
        
        print(email,password,target)
        
        L = instaloader.Instaloader()

        if not L.context.is_logged_in:
            # prompt user for login credentials
            # username = 'mailto:cyberab.best@gmail.com'
            # password = 'igat@43214'
            username = id
            password = password

            # log in and save session to file
            L.context.log("Logging in...")
            L.context.username = username
            L.context.password = password
            L.login(user=username, passwd=password)
            L.save_session_to_file("session_file")
        else:
            # load session from file
            L.load_session_from_file("session_file")

        # get a profile
        profile = instaloader.Profile.from_username(L.context, target)


        username = profile.username
        # full_name = profile.full_name
        # followers = profile.followers
        # following = profile.followees
        profile_bio = profile.biography
        # post = instaloader.Post.from_shortcode(L.context, shortcode='shortcode_of_the_post')
        
        data = [
            {"username": username,"profile_bio": profile_bio}
        ]

        # Write the data to a CSV file
        with open(f"output/{username}_profile_data.csv", "w", newline="") as csvfile:
            fieldnames = ["username", "posts"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        
    except:
        print("error in profile text")