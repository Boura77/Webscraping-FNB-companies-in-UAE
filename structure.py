
import requests

import json

import pandas as pd
 
 
url = "https://daily.noon.com/_svc/catalog/api/search"

# output = []
processed_data = {"COMPANY_NAME": ["noon"],
        "DATE": [],
        "PRODUCT_ID": [],
        "PRODUCT_NAME": [],
        "U_O_M": [],
        "PRICE": [],
        "DISCOUNTED_PRICE": [],
        "COUNTRY_OF_ORIGIN": []}
for page in [1,2,3]:

    payload = json.dumps({

        "q": "*",

        "original_q": "*",

        "brand": [],

        "category": [],

        "filterKey": [],

        "f": {

            "partner": [

                "p_45760"

            ]

        },

        "sort": {

            "by": "popularity",

            "dir": "desc"

        },

        "limit": 200,

        "page": page

    })

    headers = {

        'authority': 'daily.noon.com',

        'pragma': 'no-cache',

        'cache-control': 'no-cache, max-age=0, must-revalidate, no-store',

        'sec-ch-ua': '"Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',

        'x-locale': 'en-ae',

        'x-experience': 'daily',

        'x-content': 'desktop',

        'x-mp': 'daily',

        'x-platform': 'web',

        'x-cms': 'v2',

        'accept': 'application/json, text/plain, */*',

        'sec-ch-ua-mobile': '?0',

        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',

        'sec-fetch-site': 'same-origin',

        'sec-fetch-mode': 'cors',

        'sec-fetch-dest': 'empty',

        'referer': 'https://daily.noon.com/uae-en/search?q=*',

        'accept-language': 'en-US,en;q=0.9',

        'x-authorization': 'Bearer tMTRo6rhejVlbGknU4y9xmJhwlHK7IaYED9o1i+HUMloZHv7Bd+ORNb01Jy65u9G3G9IYPN0obA8ry+9YU1luzAD+56n8Ovt0UIITtbmdDZdmfTWd9YT8f3xLmVrVzMMyzvYKC0U2tVQqI7gDQSpK+1+rTMZj+yP8cR0k74N2kk=|EPQXwoUOmWj9DZAGg2bSjSLJ6l9BRIG99qLOzw84Gp3.QfiIWOmF2MwQGMwQTZwITZ2IGOwEWM1IjZ1gTNidzYmVjYiojIwZ2Xy9GdpNXa2Jye.9JiN1IzUIJiOicGbhJCLiQ1VKJiOiAXe0Jyesus',

        'cookie': 'next-i18next=en-AE; visitor_id=c478fc98-c9f5-4376-9721-8cc15d228601; _gcl_au=1.1.24694048.1627538969; _ga=GA1.2.1674631311.1627538970; _scid=c95f1c02-f2ee-4ce5-8919-fa8eaa8f2092; _fbp=fb.1.1627538969914.394367197; _etc=8p3Q7pQ174w6q3NG; x-available-ae=ecom-daily; __zlcmid=163kKPt8tNk2rDo; x-dsa=DS100031A; x-lat=251998495; x-lng=552715985; x-lat-old=251998495; x-lng-old=552715985; x-location-daily-ae=eyJsYXQiOiAyNTE5OTg0OTUsICJsbmciOiA1NTI3MTU5ODUsICJkc2FfY29kZSI6ICJEUzEwMDAzMUEifQ; x-daily-experience=manual-checkout; AKA_A2=A; _gcl_aw=GCL.1632120023.Cj0KCQjwv5uKBhD6ARIsAGv9a-ykfe3gqCPpJM47UO6AO2mO0Pm8Hw2_kPmm0t6jMQfQ9AKPwe5UhtgaAiDCEALw_wcB; _gid=GA1.2.710376731.1632120023; _gat_UA-84507530-22=1; RT="z=1&dm=noon.com&si=seuzl3h2gaf&ss=ktsa480k&sl=1&tt=73k&ld=73q"; _sctr=1|1632081600000; nguest=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnJhV1FpT2lJNU9EVXhaalUyTlRBeVpHRTBZakJpT0RZeVl6YzNOMlU0TkRSaU1qRmhOaUlzSW1saGRDSTZNVFl5TnpVek9EazNNSDAuam9ZVWxyQjVOalZJeWU3QW1NNjh2YTBNSDlmTVJsTGdPTVJjbUlHMTZ2QSIsImlhdCI6MTYzMjEyMDAyNH0.kpkGFMMgs69cif9WIvSO-IECMRR7PH8GOs8_iCgvzOA; _nsc=nsv1.public.eyJzdGlkIjoiODkzOWUwNzYtNGY4NC00YTU3LWIyNjctNWFiYThmMDQ4MTliIiwic2lkIjoiOTg1MWY1NjUwMmRhNGIwYjg2MmM3NzdlODQ0YjIxYTYiLCJpYXQiOjE2MzIxMjAwMjQsInZpZCI6ImM0NzhmYzk4LWM5ZjUtNDM3Ni05NzIxLThjYzE1ZDIyODYwMSIsImhvbWVwYWdlIjp7fX02bFoxUmJiRVE5dWdkeVU0bjFESVlYQ2JndVAxTnBKckNFQVhkelZWYm1zPQ.MQ; _gac_UA-84507530-22=1.1632120036.Cj0KCQjwv5uKBhD6ARIsAGv9a-ykfe3gqCPpJM47UO6AO2mO0Pm8Hw2_kPmm0t6jMQfQ9AKPwe5UhtgaAiDCEALw_wcB; _nsc=nsv1.public.eyJzdGlkIjoiNjljNGM1M2ItZjdkNS00YmU5LWI0OTUtNjBiYTQ0NWFkMzE2Iiwic2lkIjoiOTg1MWY1NjUwMmRhNGIwYjg2MmM3NzdlODQ0YjIxYTYiLCJpYXQiOjE2MzIyMDg5OTksInZpZCI6ImM0NzhmYzk4LWM5ZjUtNDM3Ni05NzIxLThjYzE1ZDIyODYwMSIsImhvbWVwYWdlIjp7fX1XQTc2T0pyRmVlQlQ1S3lGcnQ0SG1TbkdPOWhOOHB4M3VoVkVWS0wrMUE0PQ.MQ; nguest=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnJhV1FpT2lJNU9EVXhaalUyTlRBeVpHRTBZakJpT0RZeVl6YzNOMlU0TkRSaU1qRmhOaUlzSW1saGRDSTZNVFl5TnpVek9EazNNSDAuam9ZVWxyQjVOalZJeWU3QW1NNjh2YTBNSDlmTVJsTGdPTVJjbUlHMTZ2QSIsImlhdCI6MTYzMjIwODk5OX0.8ndY1xfhf5Bptx5w35ceFw5I3euY7EkfRBpMnROSWxM',

        'Content-Type': 'application/json'

    }
 
    response = requests.request("POST", url, headers=headers, data=payload)
    
    data = response.json()
    # processed_data = {"COMPANY_NAME": ["noon"],
    #     "DATE": [],
    #     "PRODUCT_ID": [],
    #     "PRODUCT_NAME": [],
    #     "U_O_M": [],
    #     "PRICE": [],
    #     "DISCOUNTED_PRICE": [],
    #     "COUNTRY_OF_ORIGIN": []}
    for items in data["hits"]:

        processed_data["PRODUCT_ID"] = items["sku"]

        processed_data["PRODUCT_NAME"] = items["name"]

        #processed_item["brand"] = items["brand"]

        processed_data["PRICE"] = items["price"]

        processed_data["DISCOUNTED_PRICE"] = items["sale_price"]

        processed_data["stock"] = items["stock"] if 'stock' in items else 0

        if "plp_specifications" in items and "Item Count" in items["plp_specifications"]:

            processed_data["U_O_M"] = items["plp_specifications"]["Item Count"]

        #if "estimated_delivery" in items:

            #processed_item["estimated_delivery"] = items["estimated_delivery"]
# noon=pd.DataFrame(output)    

# print(noon)
# print(noon)
# file_path = "C://Users//singh.b//Downloads//noon1trialfruits.csv"

# noon.to_csv(file_path, index=False)