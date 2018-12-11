#from time import time, sleep
#from random import randint
#import os

import requests
from bs4 import BeautifulSoup
import math

import pandas as pd
import csv

#header = {"Accept-Language": "en-US, en;q=0.5"}
header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
#header = { 'USER_AGENT' :  'Mozilla/5.0 (Windows NT 6.3; W…) Gecko/20100101 Firefox/59.0'}

# Lists to store the scraped data in
names = []
ttid = []
omdb = []
years = []
runtimes = []
genres = []
certificates = []
ratings = []
directors = []
stars = []
votes = []
gross = []

# Record of all movies in India, descending by box office
#url = "https://www.imdb.com/search/title?title_type=feature&release_date=2000-01-01,&countries=in&count=250&sort=boxoffice_gross_us,desc&ref_=adv_nxt"

url = "https://www.imdb.com/search/title?title_type=feature&release_date=2000-01-01,&countries=in&languages=hi&count=250"
## Above link has 4900 movies in range from 2000-01-01 to now

#url = "https://www.imdb.com/search/title?title_type=feature,tv_movie&release_date=2010-01-01,&countries=in&languages=hi&count=250"
## Above link has 2500 movies in range from 2010-01-01 to now

# This one has only 730 movies in our range
# url = "https://www.imdb.com/search/title?title_type=feature&release_date=2010-01-01,2018-12-31&has=locations&countries=in&languages=hi&locations=India&count=250"


r = requests.get(url, headers = header)
s = BeautifulSoup(r.text, 'html.parser')

div = s.find_all('div', attrs = {'class' : 'desc'})
span = div[0].find_all('span', attrs = {'class' : 'lister-current-last-item'})
text = span[0].next_sibling
text = text.split('of ')[1].split(' titles')[0].replace(',', '')

num = int(text)
lim = math.ceil(num/250)

print('No. of pages :', lim)
# Use range(1,4) for 730 url, (1,11) for 2500 url
for offset in range(1,lim+1):
    URL = url + "&page={}&ref_=adv_nxt".format(offset)

    # Make a get request
    response = requests.get(URL, headers = header)
    print(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    movie_containers = soup.find_all('div', class_ = 'lister-item mode-advanced')


    # Extract data from individual movie container
    for container in movie_containers:

        # Title
        name = container.h3.a.text.encode('utf-8').decode('utf-8')
        names.append(name)

        # IMDB tt ID
        tt = container.h3.a.get('href').encode('utf-8').decode('utf-8')
        ttid.append(tt)

        key = tt.split('/')[2].encode('utf-8').decode('utf-8')
        omdb.append(key)

        # Year
        year = container.find_all('span', class_ = 'lister-item-year text-muted unbold')[0].text.split('(')[-1].split(')')[0].encode('utf-8').decode('utf-8')
        if year == '':
            year = 0
        years.append(year)

        # Runtime
        runtime = 0
        try:
            runtime = container.find('span', class_ = 'runtime').text.split(' ')[0]
        except:
            pass
        runtimes.append(runtime)

        # Genre(s)
        genre = ''
        try:
            genre = '|'.join(container.find('span', class_ = 'genre').text.strip().split(', '))
        except:
            genre = 'No'
        genres.append(genre)

        # Certificate
        certificate = ''
        try:
            certificate = container.find('span', class_ = 'certificate').text
        except:
            certificate = 'No'
        certificates.append(certificate)

        # Rating
        rating = 0.0
        try:
            rating = container.find('div', class_ = 'inline-block ratings-imdb-rating').strong.text
        except:
            pass
        ratings.append(rating)

        # Director and Stars
        name_box = container.find_all('p', attrs = {'class' : ''})
        try:
            director = name_box[1].a.text
        except:
            director = 'No'
        directors.append(director)

        try:
            cast = name_box[1].find_all('a')[1:]
            actors = []
            for a in cast:
                actors.append(a.text)
            actors = '|'.join(actors)
            if actors=='':
                actors = 'No'
        except:
            actors = 'No'
        stars.append(actors)

        # Votes
        vote = 0
        try:
            vote = ''.join(container.find('span', attrs = {'name' : 'nv'}).text.split(','))
        except:
            pass
        votes.append(vote)

        # Gross revenue ($ x.y M)
        gross_sum = 0
        try:
            gross_sum = container.find_all('span', attrs = {'name' : 'nv'})[1].text
            gross_sum = gross_sum.split('$')[1]
            gross_sum = float(gross_sum.split('M')[0])##*1000000
        except:
            pass
        gross.append(gross_sum)
        

listing_df = pd.DataFrame({'Movie': names,
                           'ttID': ttid,
                           'OMDB': omdb,
                           'Year': years,
                           'Runtime': runtimes,
                           'Genres': genres,
                           'Certificate': certificates,
                           'Rating': ratings,
                           'Votes': votes,
                           'Gross': gross,
                           'Director': directors,
                           'Stars': stars})
print(listing_df.info())
print(listing_df)

col=['Movie', 'ttID', 'OMDB', 'Year', 'Runtime', 'Genres', 'Certificate', 'Rating', 'Votes', 'Gross', 'Director', 'Stars']

#listing_df.to_csv('movielisting.csv', encoding='utf-8', index=False)

# use full.csv when 2500+ movies
listing_df.to_csv('listingmovies.csv', encoding='utf-8', index=False, columns=col)
