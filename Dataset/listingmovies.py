#from time import time, sleep
#from random import randint
#import os

import requests
from bs4 import BeautifulSoup

import pandas as pd
import csv

header = {"Accept-Language": "en-US, en;q=0.5"}
#header = { 'USER_AGENT' :  'Mozilla/5.0 (Windows NT 6.3; W…) Gecko/20100101 Firefox/59.0'}

# Lists to store the scraped data in
names = []
ttid = []
omdb = []

url = "https://www.imdb.com/search/title?title_type=feature,tv_movie&release_date=2010-01-01,&countries=in&languages=hi&count=250"
## Above link has 2500 movies in range

# This one has only 730 movies in our range
# url = "https://www.imdb.com/search/title?title_type=feature&release_date=2010-01-01,2018-12-31&has=locations&countries=in&languages=hi&locations=India&count=250"

# Use range(1,4) for 730 url, (1,11) for 2500 url
for offset in range(1,11):
    URL = url + "&page={}&ref_=adv_nxt".format(offset)

    # Make a get request
    response = requests.get(URL, headers = header)
    print(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    movie_containers = soup.find_all('div', class_ = 'lister-item mode-advanced')


    # Extract data from individual movie container
    for container in movie_containers:

        # The name
        name = container.h3.a.text
        names.append(name)

        # The tt ID
        tt = container.h3.a.get('href')
        ttid.append(tt)

        key = tt[7:16]
        omdb.append(key)


listing_df = pd.DataFrame({'Movie': names,
                           'ttID': ttid,
                           'OMDB': omdb})
print(listing_df.info())
print(listing_df)

#listing_df.to_csv('movielisting.csv', encoding='utf-8', index=False)

# use full.csv when 2500+ movies
listing_df.to_csv('movielistingfull.csv', encoding='utf-8', index=False)
