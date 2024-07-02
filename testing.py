import requests
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas as pd


#C4

url = 'https://www.carrefouruae.com/api/v8/categories/F11600000?sortBy=relevance&currentPage=0&pageSize=2000&areaCode=Dubai%20Festival%20City%20-%20Dubai&lang=en&expressPos=015&displayCurr=AED&foodPos=072&nonFoodPos=099&latitude=25.217392942107853&longitude=55.36187758635983&requireSponsProducts=true'

payload = {}

headers = {

   'authority': 'www.carrefouruae.com',

    'accept': '*/*',

    'cache-control': 'no-cache' ,

    'dnt': '1' ,

    'pragma': 'no-cache',

    'referer': 'https://www.carrefouruae.com',

    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',

    'sec-ch-ua-mobile': '?0',

    'sec-ch-ua-platform': '"macOS"',

    'sec-fetch-dest': 'empty',

    'sec-fetch-mode': 'cors',

    'sec-fetch-site': 'same-origin',

    'service': 'algolia',

    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',

    'env': 'prod',

    'credentials': 'include',

    'userid': '',

    'storeid': 'mafuae',

    'appid': 'Reactweb',

    'token': '361f5159-b160-45ed-a744-39567985bc05',

    'accept-language': 'en-US,en;q=0.9',

    'Cookie': 'ak_bmsc=B3C50D264A0B36E8F3E3BA1102CB76B5~000000000000000000000000000000~YAAQdecVAi4iitl7AQAAUkrC6Q0O6aMVYPAjwCEikgpCdWyl8JiR+II9/PnVHvWMmluqaCTGVE1o6yl1ywp0T+c55aN+/8G2kozJViR+2fQRtK2kfYy2zcoabJbGwhtGlWl4vP4RUcrn3Wbudyq2yZ5vDGpzv6/jU8fNVJd9fVkUB8ep9Y5erJbVwyfTDDMZANIO/Gsws1tSTOvsxDcBPXhj/BaEmCnKIFyUflhhKDMQha2ggmf23EBW3DWtgrmQQ2b0VcuafzONnPWhKI8TRaLfLkl2adx3Gi4YBpaY8iPx7BRnQx+zgIdfVtjMQ3ogUdxDYsd2Lf//T9VQDjIAIWxPdXtuCwTyS3DauLr/8Q02139eyunFGpd1t0U=; cart_api=v2'

}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()

product_data = []

for items in data["products"]:

    tp = {"COMPANY_NAME": ["carrefour"],
        "DATE": [],
        "PRODUCT_ID": [],
        "PRODUCT_NAME": [],
        "U_O_M": [],
        "PRICE": [],
        "DISCOUNTED_PRICE": [],
        "COUNTRY_OF_ORIGIN": []}

    tp["PRODUCT_ID"] = items["id"]

    tp["PRODUCT_NAME"] = items["name"]
   

    if "productOrigin" in items:

        tp["COUNTRY_OF_ORIGIN"] = items["productOrigin"]

   
    if "price" in items:

        tp["PRICE"] = items["price"]["formattedValue"]

        if "discount" in items["price"]:

            tp["DISCOUNTED_PRICE"] = items["price"]["discount"]["formattedValue"]

    if "size" in items:

        tp["U_O_M"] = items["size"]

   

    product_data.append(tp)

dfc4 = pd.DataFrame(product_data)


#KIBSON
url = "https://www.kibsons.com/ecomapi/itemdetails/getItemsV2"
 
payload = '{"category":["F"],"":[""],"language":"en","searchText":""}'

headers = {

    'Connection': 'keep-alive',

    'Pragma': 'no-cache',

    'Cache-Control': 'no-cache',

    'Access-Control-Allow-Origin': '*',

    'Accept': 'application/json, text/plain, */*',

    'Content-Type': 'application/json',

    'Authorization': 'Bearer null',

    'sec-ch-ua-mobile': '?0',

    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',

    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',

    'Origin': 'https://kibsons.com',

    'Sec-Fetch-Site': 'same-site',

    'Sec-Fetch-Mode': 'cors',

    'Sec-Fetch-Dest': 'empty',

    'Referer': 'https://kibsons.com/',

    'Accept-Language': 'en-US,en;q=0.9',

    'Cookie': 'ARRAffinity=99ac31510f893deb01362c3dd468c90c01b92e5c289232ddb8c03f5a33b239f4; ARRAffinitySameSite=99ac31510f893deb01362c3dd468c90c01b92e5c289232ddb8c03f5a33b239f4'

}
 
response = requests.request("POST", url, headers=headers, data=payload)

data = response.json()
 
product_data1 = []

for items in data["data"]:

    tp = {"COMPANY_NAME": ["KIBSON"],
        "DATE": [],
        "PRODUCT_ID": [],
        "PRODUCT_NAME": [],
        "U_O_M": [],
        "PRICE": [],
        "DISCOUNTED_PRICE": [],
        "COUNTRY_OF_ORIGIN": []}

    tp["PRODUCT_ID"] = items["serialNo"]

    tp["PRODUCT_NAME"] = items["stockDesc"]

    tp["PRICE"] = items["stockRate"]

    if "stockPromotionRate" in items:

        tp["DISCOUNTED_PRICE"] = items["stockPromotionRate"]

    #tp["ribbonText"] = items["ribbonText"]

    tp["U_O_M"] = items["stockShortDetail"]

    tp["COUNTRY_OF_ORIGIN"] = items["stockOrigin"]

    product_data1.append(tp)

dfk = pd.DataFrame(product_data1)




url = "https://www.kibsons.com/ecomapi/itemdetails/getItemsV2"
 
payload = '{"category":["V"],"":[""],"language":"en","searchText":""}'

headers = {

    'Connection': 'keep-alive',

    'Pragma': 'no-cache',

    'Cache-Control': 'no-cache',

    'Access-Control-Allow-Origin': '*',

    'Accept': 'application/json, text/plain, */*',

    'Content-Type': 'application/json',

    'Authorization': 'Bearer null',

    'sec-ch-ua-mobile': '?0',

    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',

    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',

    'Origin': 'https://kibsons.com',

    'Sec-Fetch-Site': 'same-site',

    'Sec-Fetch-Mode': 'cors',

    'Sec-Fetch-Dest': 'empty',

    'Referer': 'https://kibsons.com/',

    'Accept-Language': 'en-US,en;q=0.9',

    'Cookie': 'ARRAffinity=99ac31510f893deb01362c3dd468c90c01b92e5c289232ddb8c03f5a33b239f4; ARRAffinitySameSite=99ac31510f893deb01362c3dd468c90c01b92e5c289232ddb8c03f5a33b239f4'

}
 
response = requests.request("POST", url, headers=headers, data=payload)

data = response.json()
 
product_data = []

for items in data["data"]:

    tp = {"COMPANY_NAME": ["KIBSON"],
        "DATE": [],
        "PRODUCT_ID": [],
        "PRODUCT_NAME": [],
        "U_O_M": [],
        "PRICE": [],
        "DISCOUNTED_PRICE": [],
        "COUNTRY_OF_ORIGIN": []}

    tp["PRODUCT_ID"] = items["serialNo"]

    tp["PRODUCT_NAME"] = items["stockDesc"]

    tp["PRICE"] = items["stockRate"]

    if "stockPromotionRate" in items:

        tp["DISCOUNTED_PRICE"] = items["stockPromotionRate"]

    #tp["ribbonText"] = items["ribbonText"]

    tp["U_O_M"] = items["stockShortDetail"]

    tp["COUNTRY_OF_ORIGIN"] = items["stockOrigin"]

    #tp["stockUnits"] = items["stockUnits"]

    #tp["category"] = items["family_en_desc"]

    product_data.append(tp)

dfk = pd.DataFrame(product_data)

df12 = pd.concat([dfc4, dfk], ignore_index=True)
print(df12)

#LULU
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

# url = "https://www.luluhypermarket.com/en-ae/grocery-fresh-food-fruits-vegetables/c/HY00216090?q=%3Adiscount-desc%3Acategory%3AHY00216102%3Acategory%3AHY00216101&text=#"
HEAD = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'}
# html_text = requests.get(url, headers=HEAD)

# soup = BeautifulSoup(html_text.text, "html.parser") 


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

data1 = {"COMPANY_NAME": ["LULU"],
        "DATE": [],
        "PRODUCT_ID": [],
        "PRODUCT_NAME": [],
        "U_O_M": [],
        "PRICE": [],
        "DISCOUNTED_PRICE": [],
        "COUNTRY_OF_ORIGIN": []}

for link in href_links:
    new_response= requests.get(link, headers=HEAD)
    final_soup = BeautifulSoup(new_response.content, "html.parser")
    data1['PRODUCT_NAME'].append(get_name(final_soup))  
    data1['PRICE'].append(get_og_price(final_soup))  
    data1['DISCOUNTED_PRICE'].append(get_current_price(final_soup)) 

df3 = pd.DataFrame.from_dict(data1)


df13 = pd.concat([df12, df3], ignore_index=True)
print(df13)




