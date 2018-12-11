import requests
import json
from bs4 import BeautifulSoup

import pandas as pd

from time import time, sleep
import random

# Sample API use for GoG2
# url = 'http://www.omdbapi.com/?i=tt3896198&apikey=d414a8e8'
key = 'd414a8e8'
# key = 'e7a432fa'
# key = '9043a162'
# key = '4aea87fe'
url = 'http://www.omdbapi.com/'
#header = { 'USER_AGENT' :  'Mozilla/5.0 (Windows NT 6.3; W…) Gecko/20100101 Firefox/59.0', "Accept-Language": "en-US, en;q=0.5"}
#header = { 'USER_AGENT' :  'Mozilla/5.0 (Windows NT 6.3; W…) Gecko/20100101 Firefox/59.0'}

import csv
file = open("./listingmovies.csv", "r")

#file = pd.read_csv("movielisting.csv")

#file = open("movielistingfull.csv", "r")

ttid = []
reader = csv.reader(file)


def get_url(url):
    response = requests.get(url)
    content = response.content.encode("utf8")
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


for row in reader:
    ttid.append(row[2])

# Slicing off the Column Name 
# ttid = ttid[1:]

MovieName = []
ReleaseYear = []
Rated = []
ReleaseDate = []
Runtime = []
Genre = []
Director = []
Writers = []
Actors = []
Plot = []
Language = []
Country = []
Awards = []
imdbRatings = []
tomatoesRatings = []
metaScores = []
imdbVotes = []
imdbID = []
Type = []
DVD = []
BoxOffice = []
Production = []
Website = []

num = len(ttid)

# Play with this to create dataset
for i in range(3001,4001):
    
        URL = url + "?i={}&apikey={}".format(ttid[i],key)
        print(i,URL)

        response = requests.get(URL)
        try:
            js = json.loads(response.text)
            print(js)
        except JSONDecodeError:
                continue
        #print(js)
    
    #if js["Response"] is True:
        try:
            title = js["Title"]
            MovieName.append(title)
        except KeyError:
            MovieName.append(None)

        try:
            year = js["Year"]
            ReleaseYear.append(year)
        except KeyError:
            ReleaseYear.append(None)

        try:
            rated = js["Rated"]
            Rated.append(rated)
        except KeyError:
            Rated.append(None)

        try:
            released = js["Released"]
            ReleaseDate.append(released)
        except KeyError:
            ReleaseDate.append(None)

        try:
            runtime = js["Runtime"]
            Runtime.append(runtime)
        except KeyError:
            Runtime.append(None)

        try:
            genre = js["Genre"]
            Genre.append(genre)
        except KeyError:
            Genre.append(None)

        try:
            director = js["Director"]
            Director.append(director)
        except KeyError:
            Director.append(None)

        try:
            writers = js["Writer"]
            Writers.append(writers)
        except KeyError:
            Writers.append(None)

        try:
            actors = js["Actors"]
            Actors.append(actors)
        except KeyError:
            Actors.append(None)

        try:
            plot = js["Plot"]
            Plot.append(plot)
        except KeyError:
            Plot.append(None)

        try:
            lang = js["Language"]
            Language.append(lang)
        except KeyError:
            Language.append(None)

        try:
            awards = js["Awards"]
            Awards.append(awards)
        except KeyError:
            Awards.append(None)

        try:
            imdbscore = js["imdbRating"]
            imdbRatings.append(imdbscore)
        except KeyError:
            imdbRatings.append(None)

        try:
            rottenscore = js["Ratings"][1]["Value"]
            tomatoesRatings.append(rottenscore)
        except IndexError:
            tomatoesRatings.append(None)
        except KeyError:
            tomatoesRatings.append(None)

        try:
            metascore = js["Metascore"]
            metaScores.append(metascore)
        except KeyError:
            metaScores.append(None)

        try:
            imdbvotes = js["imdbVotes"]
            imdbVotes.append(imdbvotes)
        except KeyError:
            imdbVotes.append(None)

        try:
            imdbid = js["imdbID"]
            imdbID.append(imdbid)
        except KeyError:
            imdbID.append(ttid[i])

        try:
            movtype = js["Type"]
            Type.append(movtype)
        except KeyError:
            Type.append(None)

        try:
            dvd = js["DVD"]
            DVD.append(dvd)
        except KeyError:
            DVD.append(None)

        try:
            boxoffice = js["BoxOffice"]
            BoxOffice.append(boxoffice)
        except KeyError:
            BoxOffice.append(None)

        try:
            prod = js["Production"]
            Production.append(prod)
        except KeyError:
            Production.append(None)

        try:
            site = js["Website"]
            Website.append(site)
        except KeyError:
            Website.append(None)

    
movie_data = pd.DataFrame({'Movie': MovieName,
                           'Year': ReleaseYear,
                           'Rated': Rated,
                           'Released': ReleaseDate,
                           'Runtime': Runtime,
                           'Genre': Genre,
                           'Director': Director,
                           'Writers': Writers,
                           'Actors': Actors,
                           'Plot': Plot,
                           'Language': Language,
                           'Awards': Awards,
                           'IMDB_Rating': imdbRatings,
                           'Rotten Tomatoes': tomatoesRatings,
                           'MetaCritic': metaScores,
                           'IMDB_votes': imdbVotes,
                           'IMDB_ID': imdbID,
                           'Type': Type,
                           'DVD': DVD,
                           'Box_Office': BoxOffice,
                           'Production': Production,
                           'Website': Website
                           })
print(movie_data.info())
#print(movie_data)

movie_data.to_csv('movies4k.csv', encoding='utf-8', index=False)

# Note to self : older version of pandas rearranges the data frame alphabetically
# Update to 0.23.0 to retain the insertion order
