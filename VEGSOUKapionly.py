import requests
import bs4 as BeautifulSoup
import pandas as pd
page_numbers= range(1,6)
all_external_urls = []
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



 data = response.json()
 

 for item in data["data"]["hits"]:
    
    external_url = item["externalUrl"]

    
    all_external_urls.append(external_url)


data1 = {"COMPANY":["VegetableSouk"],"PRODUCT_NAME": [],"PRICE": [], "COUNTRY OF ORIGIN":[]}

def get_title(soup):
   try:
      title=soup.find('div', class_='pdp-heart').text.strip()
      return title
   except AttributeError:
        return ""
   
def get_price(soup):
    try:
        price = soup.find('span', class_='t3-mainPrice me-3').text.strip()
        return price
    except AttributeError:
        return ""

def get_country(soup):
    try:
      country=soup.find('div', class_='country').text.strip()
      return country
    except AttributeError:
        return ""


for new_url in all_external_urls:
    response1 = requests.get(new_url, headers=HEAD)
    new_soup = BeautifulSoup(response1.text, "html.parser")
    data1['PRODUCT_NAME'].append(get_title(new_soup))
    data1['PRICE'].append(get_price(new_soup))
    data1['COUNTRY OF ORIGIN'].append(get_country(new_soup))


df_vs_veg= pd.DataFrame.from_dict(data1)
print(df_vs_veg)