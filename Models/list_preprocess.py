import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ds_full = pd.read_csv('./listingmovies.csv')

ds = ds_full[ds_full.Gross != 0]

genre = ds.Genres.str.split('|', expand=True).stack()
star = ds.Stars.str.split(r'|', expand=True).stack().reset_index(level=1, drop=True).to_frame('Stars')
cert = ds.Certificate.str.split('|', expand=True).stack()
direc = ds.Director.str.split('|', expand=True).stack()
year = ds.Year.str.split('|', expand=True).stack()
run = ds.Runtime.str.split(' ', expand=True).stack()

df_genre = pd.get_dummies(genre, prefix='g').groupby(level=0).sum()
df_star = pd.get_dummies(star, prefix='s', columns=['Stars']).groupby(level=0).sum()
df_cert = pd.get_dummies(cert, prefix='c').groupby(level=0).sum()
df_dir = pd.get_dummies(direc, prefix='d').groupby(level=0).sum()
df_year = pd.get_dummies(year, prefix='y').groupby(level=0).sum()
df_runtime = pd.get_dummies(run, prefix='r').groupby(level=0).sum().drop(['r_min'], axis=1)

movie = ds.Movie
gross = ds.Gross
rating = ds.Rating
vote = ds.Votes

cleaned_df = pd.concat([movie, gross, rating, vote, df_genre, df_cert, df_year, df_runtime, df_dir, df_star], axis=1)

cleaned_df.to_csv('preprocessedmovies.csv', encoding='utf-8', index=False)

