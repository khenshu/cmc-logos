#!/usr/bin/env python3
import urllib, requests, re
import os
from bs4 import BeautifulSoup


IMG_SIZE = "32x32"

def get_logo_ids():
    logo_dict = {}
    result = requests.get("https://coinmarketcap.com/coins/views/all/")
    c = result.content
    soup = BeautifulSoup(c)
    trows = soup.find_all("tr", id=re.compile("id"))
    for trow in trows:
        coin_id = trow.get("id").split("-", 1)[-1]
        #the logo_div tag contains the logo id
        logo_div = trow.find("div", class_="currency-logo-sprite")
        match = re.search("s-s-([0-9]*)", str(logo_div))
        logo_id = match.group(1)
        logo_dict[coin_id] = logo_id
    return logo_dict

def download_logos(logo_dict, img_size):
    base_img_url = "https://s2.coinmarketcap.com/static/img/coins/"
    #create a folder to save the files
    if not os.path.exists(img_size):
        os.makedirs(img_size)
        print(img_size+" folder created")
    for coin_id, logo_id in logo_dict.items():
        #construct the logo image url
        img_url = base_img_url+img_size+"/"+logo_id+".png"
        file_path = img_size+"/"+coin_id+".png"
        #download and save
        try:
            urllib.request.urlretrieve(img_url, file_path)
            print(img_url+" --> "+file_path)
        except Exception as e:
            print(e)
            continue


if __name__ == "__main__":
    logo_dict = get_logo_ids()
    download_logos(logo_dict, IMG_SIZE)
