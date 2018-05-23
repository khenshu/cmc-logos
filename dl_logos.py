# ---------- DEPENDENCIES ---------- #

import requests
from bs4 import BeautifulSoup
import re
import urllib
import os

# ---------- GV's ---------- #

IMG_SIZE = "64x64"                                                              # STRING  --> 16x16, 32x32, 64x64 or 128x128.
IMG_DIRECTORY = ""                                                              # STRING  --> The directory you's like the images to be saved into. Make sure that this directory exists.
SEPERATE = True                                                                 # BOOLEAN --> Specifies whether you'd like images with different sizes to be grouped into a different folder or just replace the current image on re-run.

# ---------- FUNCTIONS ---------- #

def main():
    ''' Pulls full crypto list from CMC and parses to extract name and image id
    of each asset. Downloads and saves image to specified folder.'''

    print('Starting...')

    logos = {}
    try:
        cmc = requests.get("https://coinmarketcap.com/all/views/all/")          # Gets cmc page.
    except Exception as e:
        raise Exception('ERROR --> Could not get CMC main page: ' + str(e))

    c = cmc.content
    soup = BeautifulSoup(c, 'html.parser')                                      # Parses page content.
    trows = soup.find_all("tr", id=re.compile("id"))                            # Finds the id of each table row on the page.

    for trow in trows:                                                          # Iterates rows.

        coin_id = trow.get("id").split("-", 1)[-1]
        logo_div = trow.find("div", class_="logo-sprite")
        match = re.search("s-s-([0-9]*)", str(logo_div))
        try:
            logo_id = match.group(1)
        except:
            logo_id = match

        logos[coin_id] = logo_id                                                # Commits coinId and logoId pair to logos list.

    base_img_url = "https://s2.coinmarketcap.com/static/img/coins/"             # Image location on CMC website.

    for coin_id, logo_id in logos.items():

        img_url = base_img_url + IMG_SIZE + "/" + logo_id + ".png"              # Specifies actual url of image.

        file_path = IMG_DIRECTORY
        if SEPERATE == True:
            file_path = IMG_DIRECTORY + IMG_SIZE + "/"
            if not os.path.exists(file_path):
                os.makedirs(file_path)

        filename = coin_id + '.png'
        fullfilename = os.path.join(file_path, filename)

        print("Saving: " + img_url + " Into --> " + file_path)

        try:
            urllib.request.urlretrieve(img_url, fullfilename)
            print("Saved.")
        except Exception as e:
            print("!!! Not Saved: " + str(e))
            continue

# ---------- Initiator ---------- #

if __name__ == '__main__':
    main()
