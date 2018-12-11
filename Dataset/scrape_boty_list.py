import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import csv

ds = pd.read_csv('./boty_url.csv')
movie_url = ds.BOTY

header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

# Lists to store the scraped data in
release_dates = []
stars = []
directors = []
budget = []
box_office_india = []
box_office_worldwide = []
genres = []

for url in movie_url:
    print(url)
    
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    table = soup.find('table', attrs = {'id' : 'movie-info'})
    
    rows = table.find_all('tr')
    release_dates.append(rows[0].td.text.strip())
    stars.append(rows[1].td.text.strip())
    directors.append(rows[2].td.text.strip())
    budget.append(rows[3].td.text.strip())
    box_office_india.append(rows[4].td.text.strip())
    box_office_worldwide.append(rows[5].td.text.strip())
    genres.append(rows[6].td.text.strip())
    
     

df = pd.DataFrame({'Movie': ds.Movie,
                   'BOTY': ds.BOTY,
                   'Year': ds.Year,
                   'Release': release_dates,
                   'Genres': genres,
                   'Budget': budget,
                   'Box_Office_India': box_office_india,
                   'Box_Office_Worldwide': box_office_worldwide,
                   'Director': directors,
                   'Stars': stars})
print(df.info())
print(df)

col=['Movie', 'BOTY', 'Year', 'Release', 'Genres', 'Budget', 'Box_Office_India', 'Box_Office_Worldwide', 'Director', 'Stars']
df.to_csv('boty_full.csv', encoding='utf-8', index=False, columns=col)
