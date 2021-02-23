# Convert Jupyter Notebook to Python
# -------------------------------------------------------------
# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import pandas as pd
from time import sleep


# NASA Mars Web Scraper
# ---------------------------------------------------------------

def scrape():

    # Set Executable Path & Initialize Chrome Browser
    executable_path = {"executable_path": "./chromedriver.exe"}
    browser = Browser("chrome", **executable_path)

    # Create empty dictionary to hold all variables
    mars_data = {}


    # Visit Nasa news url through splinter module
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(browser.html, 'html.parser')

    #Find latest news title 
    news_title = soup.find_all('div', class_='content_title')
    news_title[1].get_text()
    title = news_title[1].get_text()
    mars_data["title"] = title

    #Find latest news description
    news_p = soup.find_all('div', class_='article_teaser_body')
    news_p[1].get_text()
    mars_data["news_p"] = news_p

#COPY REMAINING IPYNB
return mars_data