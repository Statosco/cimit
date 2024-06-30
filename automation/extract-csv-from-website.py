import pandas as pd

read = pd.read_csv('https://www.football-data.co.uk/new_league_fixtures.csv')
v =read.rename(columns={'MaxA' : 'maximum'}, inplace=True)
print(read)