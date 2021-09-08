from bs4 import BeautifulSoup
import requests

response = requests.get("https://horoguides.com/tw/brands_list")
soup = BeautifulSoup(response.text, "html.parser")
brands = soup.find_all("div", {"class": "brand name"})
with open("brandlist.txt","w") as bl:
    for brand in brands:
        if len(brand.text) <= 1:
            continue
        bl.write(brand.text+"\n")