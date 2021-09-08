from selenium import webdriver
import requests
import os

with open ("brandlist_url.txt","r") as burl:
    brandurls = burl.readlines()

for brand in brandurls:

    brand = brand.split("\n")[0]
    url = "https://horoguides.com/tw/w_watch_finder.php?getBrands="+brand

    driver = webdriver.Chrome("/***/chromedriver")
    driver.get(url)

    # pages = driver.find_element_by_class_name("FwDataPages")
    # pagenum = int(pages.text.split("/")[1])
    # i = 1

    # while(i < pagenum):
    #     if (driver.find_element_by_id("moreBtn_1") != None):
    #         morebutton = driver.find_element_by_id("moreBtn_1")
    #         morebutton.click()
    #     i += 1


    imgs = driver.find_elements_by_css_selector(".fWatchImg + img")
    for img in imgs:
        link = img.get_attribute("src")
        name = img.get_attribute("alt")
        imgfile = requests.get(link)
        imgpath = "image/"+brand.split("%")[0]
        if not os.path.exists(imgpath):
            os.mkdir(imgpath)
        with open(imgpath+"/"+name+".jpg", "wb") as file:
            file.write(imgfile.content) 

    driver.close()