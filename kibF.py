import requests
import os
import pandas as pd
 
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
 
output = []

for items in data["data"]:

    item = {}

    item["id"] = items["serialNo"]

    item["name"] = items["stockDesc"]

    item["price"] = items["stockRate"]

    if "stockPromotionRate" in items:

        item["special_price"] = items["stockPromotionRate"]

    item["ribbonText"] = items["ribbonText"]

    item["size"] = items["stockShortDetail"]

    item["origin"] = items["stockOrigin"]

    item["stockUnits"] = items["stockUnits"]

    item["category"] = items["family_en_desc"]

    output.append(item)

kibson = pd.DataFrame(output)  

print(kibson)
file_path = "C://Users//singh.b//Downloads//kibsonfruits.csv"

kibson.to_csv(file_path, index=False)