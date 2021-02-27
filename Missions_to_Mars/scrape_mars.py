# Convert Jupyter Notebook to Python
# -------------------------------------------------------------
# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd
from random import randint
from time import sleep


# NASA Mars Web Scraper
# ---------------------------------------------------------------

def scrape():

    # Set Executable Path & Initialize Chrome Browser
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path)

    # Create empty dictionary to hold all variables
    mars_data = {}


    # Visit Nasa news url through splinter module
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    sleep(randint(1,5))

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(browser.html, 'html.parser')

    #Find latest news title 
    news_title = soup.find_all('div', class_='content_title')
    news_title[1].get_text()
    title = news_title[1].get_text()
    mars_data["title"] = title

    #Find latest news description
    news_article = soup.find('div', class_='article_teaser_body')
    news_p= news_article.get_text()
    mars_data["news_p"] = news_p
    

    # Visit JPL Mars Space Images
    jpl_img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_img_url)
    sleep(randint(1,5))

    # Sort for latest Mars photos in gallery 
    browser.find_by_id('filter_Mars').first.click()
    sleep(randint(1,5))

    #Set up new html/bs
    featured_img_html = browser.html
    img_soup = BeautifulSoup(featured_img_html, 'html')
    featured_img_url = img_soup.find('img', class_="BaseImage object-contain")["src"]
    mars_data["image"] = featured_img_url

    # Visit Mars facts url through splinter module
    facts_url = 'https://space-facts.com/mars/'
    browser.visit(facts_url)
    sleep(randint(1,5))

    # Scrape the table containing facts about the planet including Diameter, Mass, etc.and turn into HTML table string
    facts_table = pd.read_html(facts_url)
    mars_facts_html = facts_table[0].to_html()
    mars_data["facts_table"]= mars_facts_html 

    #Set an empty list to hold urls
    hemis_img_urls = []

    #Visit main site
    hemis_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemis_url)
    sleep(randint(1,5))

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #Locate each of the divs with hemisphere info
    base_url = "https://astrogeology.usgs.gov"
    results = soup.find_all("div", class_='description')
    
    #Runs through each hemisphere div, clicks in to find link to full size image URL, title of Hemisphere, and appends the dictionary
    for result in results:
        
        hemi_title = result.find('h3').text

        img_page_url = base_url + result.find('a')['href']
        
        response = requests.get(img_page_url)
        img_page_soup = BeautifulSoup(response.text, 'html.parser')
        
        hemi_img_url = img_page_soup.find('ul').li.a['href']
        
        hemi_img_dict = {'title': hemi_title, 
                    'img_url': hemi_img_url}
        
        hemis_img_urls.append(hemi_img_dict)
    
    return(mars_data)