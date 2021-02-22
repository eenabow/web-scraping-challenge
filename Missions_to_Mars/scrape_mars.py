# Convert Jupyter Notebook to Python 
#-------------------------------------------------------------
# Dependencies and Setup
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import datetime as dt

# Set Executable Path & Initialize Chrome Browser
executable_path = {"executable_path": "./chromedriver.exe"}
browser = Browser("chrome", **executable_path)

#  The default port used by MongoDB is 27017
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# NASA Mars Web Scraper
#---------------------------------------------------------------

def scrape():
    #DOWNLOAD IPYNB AS PYTHON HERE 

