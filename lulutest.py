from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='C:/Users/singh.b/Downloads/hi/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
scroll_pause_time = 1
driver.get("https://www.luluhypermarket.com/en-ae/grocery-fresh-food-fruits-vegetables/c/HY00216090")


SCROLL_PAUSE_TIME = 10


last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    
    time.sleep(SCROLL_PAUSE_TIME)

   
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

href_links = []  
product_links = driver.find_elements(By.CLASS_NAME, 'js-gtm-product-link')

for link in product_links:
     href = link.get_attribute("href")  
     href_links.append(href)  

     print(href_links)

print(href_links[-1])

from bs4 import BeautifulSoup
import requests

url = "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-fruits-vegetables/c/HY00216090?q=%3Adiscount-desc%3Acategory%3AHY00216102%3Acategory%3AHY00216101&text=#"
HEAD = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'}
html_text = requests.get(url, headers=HEAD)

soup = BeautifulSoup(html_text.text, "html.parser") 


import pandas as pd



def get_name(soup):  
    try:
        return soup.find("h1", class_='product-name').text.strip()
    except AttributeError:
        return ""

def get_og_price(soup):  
    try:
        return soup.find('span', class_="off" ).text
    except AttributeError:
        return ""

def get_current_price(soup):  
    try:
        return soup.find('span', class_="current").find('span', class_='item price').text
    except AttributeError:
        return ""

data = {"PRODUCT_NAME": [], "PRICE": [], "DISCOUNTED_PRICE": []}

for link in href_links:
    new_response= requests.get(link, headers=HEAD)
    final_soup = BeautifulSoup(new_response.content, "html.parser")
    data['PRODUCT_NAME'].append(get_name(final_soup))  
    data['PRICE'].append(get_og_price(final_soup))  
    data['DISCOUNTED_PRICE'].append(get_current_price(final_soup)) 

df = pd.DataFrame.from_dict(data)

print(df)
