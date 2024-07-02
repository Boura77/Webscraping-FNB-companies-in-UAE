import requests
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas as pd

#carrefour

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

df = pd.DataFrame(product_data)
print(df)


