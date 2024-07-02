import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
page_numbers= range(1,6)
all_external_urlsF = []
url = "https://cst0dljetj.execute-api.ap-south-1.amazonaws.com/Production/content/zWOrH-c5P942toMgFbh/listproducts"

HEAD = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}

for page_number in page_numbers:
 querystring = {"id":"60b5e1fb88261c0012c69539","perPage":"48","page":str(page_number)}

 payload = ""
 headers = {
    "authority": "cst0dljetj.execute-api.ap-south-1.amazonaws.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NWIzNmRiMjliZTNkYzAwMTk3N2ZkMDkiLCJuYW1lIjoiZ3Vlc3QtbXdaQ3p0ekF5IiwiZW1haWwiOiJndWVzdC1td1pDenR6QXkiLCJpYXQiOjE3MDYyNTc4NDJ9.MyxizHNCVcHEM-9_YxMWBsp9xI-KC_HSl3__To3J0FY",
    "cache-control": "no-cache",
    "origin": "https://www.vegetablesouk.com",
    "pragma": "no-cache",
    "referer": "https://www.vegetablesouk.com/",
    "sec-ch-ua": "^\^Not",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    "x-api-key": "Dnx6IkTNgO8vOQrgKwyza6RxfLfJA8Mu3RetJcGy"
  }

 response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

 dataVF = response.json()
 

 for item in dataVF["data"]["hits"]:
    
    external_url = item["externalUrl"]

    
    all_external_urlsF.append(external_url)

def get_title(soup):
   try:
      title=soup.find('div', class_='pdp-heart').text.strip()
      return title
   except AttributeError:
        return ""
   
def get_price(soup):
    try:
        price = soup.find('span', class_='t3-mainPrice me-3').text.strip()
        import re
        match = re.search(r'\d+(?:\.\d+)?', price)  
        if match:
         pricevegf = match.group()  
         return pricevegf
    except AttributeError:
        return ""

def get_country(soup):
    try:
      country=soup.find('div', class_='country').text.strip()
      return country
    except AttributeError:
        return ""

def get_quantity(soup):
    try:
        quant = soup.find('div', class_='approx-div').find('p').text.strip()
        if "Notes" in quant:
            quant_clean=quant.split("Notes")[1].strip()
            return quant_clean
        else:
            return quant
    except AttributeError:
        return ""
    
def get_date():
        return datetime.now().date()
    

def get_company1():
    try:
        return "VegetableSouk"
    except AttributeError:
        return ""
def get_1():
    try:
        return None
    except AttributeError:
        return ""
    
vegsoukF = {"COMPANY_NAME": [],
        "DATE": [],
        "PRODUCT_ID": [],
        "PRODUCT_NAME": [],
        "U_O_M": [],
        "PRICE": [],
        "DISCOUNTED_PRICE": [],
        "COUNTRY_OF_ORIGIN": []}

for new in all_external_urlsF:
    response1 = requests.get(new, headers=HEAD)
    new_soup = BeautifulSoup(response1.text, "html.parser")
    vegsoukF['PRODUCT_NAME'].append(get_title(new_soup))
    vegsoukF['PRICE'].append(get_price(new_soup))
    vegsoukF['COUNTRY_OF_ORIGIN'].append(get_country(new_soup))
    vegsoukF['COMPANY_NAME'].append(get_company1())
    vegsoukF['DATE'].append(get_date())
    vegsoukF['PRODUCT_ID'].append(get_1())
    vegsoukF['U_O_M'].append(get_quantity(new_soup))
    vegsoukF['DISCOUNTED_PRICE'].append(get_1())

dfvegf = pd.DataFrame(vegsoukF)

print(dfvegf)


import requests
page_numbers= range(1,5)
url = "https://cst0dljetj.execute-api.ap-south-1.amazonaws.com/Production/content/zWOrH-c5P942toMgFbh/listproducts"

all_external_urlsV = []
for page_number in page_numbers:
 querystring = {"id":"60c4a9c1752cd20012f36b93","perPage":"48","page":str(page_number)}

 payload = ""
 headers = {
    "authority": "cst0dljetj.execute-api.ap-south-1.amazonaws.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NWIzNmRiMjliZTNkYzAwMTk3N2ZkMDkiLCJuYW1lIjoiZ3Vlc3QtbXdaQ3p0ekF5IiwiZW1haWwiOiJndWVzdC1td1pDenR6QXkiLCJpYXQiOjE3MDYyNTc4NDJ9.MyxizHNCVcHEM-9_YxMWBsp9xI-KC_HSl3__To3J0FY",
    "cache-control": "no-cache",
    "origin": "https://www.vegetablesouk.com",
    "pragma": "no-cache",
    "referer": "https://www.vegetablesouk.com/",
    "sec-ch-ua": "^\^Not",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    "x-api-key": "Dnx6IkTNgO8vOQrgKwyza6RxfLfJA8Mu3RetJcGy"
}

 response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

#print(response.text)

 dataVV = response.json()

 for item in dataVV["data"]["hits"]:
    
    external_url = item["externalUrl"]

    
    all_external_urlsV.append(external_url)

def get_title(soup):
   try:
      title=soup.find('div', class_='pdp-heart').text.strip()
      return title
   except AttributeError:
        return ""
   
def get_price(soup):
    try:
        price = soup.find('span', class_='t3-mainPrice me-3').text.strip()
        import re
        match = re.search(r'\d+(?:\.\d+)?', price)  
        if match:
         price_vegv = match.group()  
         return price_vegv
    except AttributeError:
        return ""

def get_country(soup):
    try:
      country=soup.find('div', class_='country').text.strip()
      return country
    except AttributeError:
        return ""

def get_company1():
    try:
        return "VegetableSouk"
    except AttributeError:
        return ""

def get_quantity(soup):
    try:
        quant = soup.find('div', class_='approx-div').find('p').text.strip()
        if "Notes" in quant:
            quant_clean=quant.split("Notes")[1].strip()
            return quant_clean
        else:
            return quant
    except AttributeError:
        return ""

def get_date():
        return datetime.now().date()

def get_1():
    try:
        return None
    except AttributeError:
        return ""
    
soukV = {"COMPANY_NAME": [],
        "DATE": [],
        "PRODUCT_ID": [],
        "PRODUCT_NAME": [],
        "U_O_M": [],
        "PRICE": [],
        "DISCOUNTED_PRICE": [],
        "COUNTRY_OF_ORIGIN": []}

for new in all_external_urlsV:
    response1 = requests.get(new, headers=HEAD)
    new_soup = BeautifulSoup(response1.text, "html.parser")
    soukV['PRODUCT_NAME'].append(get_title(new_soup))
    soukV['PRICE'].append(get_price(new_soup))
    soukV['COUNTRY_OF_ORIGIN'].append(get_country(new_soup))
    soukV['COMPANY_NAME'].append(get_company1())
    soukV['DATE'].append(get_date())
    soukV['PRODUCT_ID'].append(get_1())
    soukV['U_O_M'].append(get_quantity(new_soup))
    soukV['DISCOUNTED_PRICE'].append(get_1())

dfvegv = pd.DataFrame(soukV)

df4 = pd.concat([dfvegf, dfvegv], ignore_index=True)
print(df4)