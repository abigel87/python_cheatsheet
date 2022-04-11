_# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 19:28:04 2022

@author: PocsG
"""

#https://realpython.com/python-data-cleaning-numpy-pandas/

import pandas as pd
import numpy as np

df = pd.read_csv('D:\Documents\misc\python_practice\BL-Flickr-Images-Book.csv')
df_head = df.head()

to_drop = ['Edition Statement',
            'Corporate Author',
            'Corporate Contributors',
            'Former owner',
            'Engraver',
            'Contributors',
            'Issuance type',
            'Shelfmarks']

df.drop(to_drop, inplace = True, axis = 1)
df.drop(columns = to_drop, inplace = True)

df["Identifier"].is_unique
df.set_index("Identifier", inplace = True)


df.iloc[234]
df.loc[1905: ,"Date of Publication"].head(10)

regex = r'^(\d{4})'
extr = df['Date of Publication'].str.extract(regex, expand = False)
extr.head(10)

df.loc[1905:, 'Date of Publication'].head(10)
extr.loc[(extr.str.len() != 4) & (extr == extr)]

import math
math.isnan(extr.loc[667])

df["Place of Publication"].head(10)
df.loc[4157862]

pub = df["Place of Publication"]
london = pub.str.contains("London")
oxford = pub.str.contains("Oxford")

london.sum()
oxford.sum()
df["Place of Publication"] = np.where(london, "London", 
         np.where(oxford, "Oxford", pub.str.replace("-"," ")))

df[(df["Place of Publication"]!="London") & (df["Place of Publication"]!="Oxford")].head(10)
pub_places = df["Place of Publication"].unique()
pub_places.sort()

bp = df.loc[df["Place of Publication"] == "Budapest"]
del(bp)

university_towns = []
with open('D:/Documents/misc/python_practice/university_towns.txt') as file:
    for line in file:
        if'[edit]' in line:
            # Remember this `state` until the next is found
            state = line
        else:
             # Otherwise, we have a city; keep `state` as last-seen
             university_towns.append((state, line))


university_towns[:5]
towns_df = pd.DataFrame(university_towns, columns=["State", "RegionName"])

def get_citystate(item):
    if '(' in item:
        return item[:item.find(" (")]
    elif '[' in item:
        return item[:item.find("[")]
    else:
        return item
    
towns_df = towns_df.applymap(get_citystate)
(towns_df["State"] + towns_df["RegionName"]).is_unique

olympics_df = pd.read_csv("D:/Documents/misc/python_practice/olympics.csv", header = 1)
olympics_df.head(10)

new_names = {"Unnamed: 0" : "Country",
             '? Summer': 'Summer Olympics',
               '01 !': 'Gold',
               '02 !': 'Silver',
               '03 !': 'Bronze',
               '? Winter': 'Winter Olympics',
               '01 !.1': 'Gold.1',
               '02 !.1': 'Silver.1',
               '03 !.1': 'Bronze.1',
               '? Games': '# Games',
               '01 !.2': 'Gold.2',
               '02 !.2': 'Silver.2',
               '03 !.2': 'Bronze.2'}

olympics_df.rename(columns=new_names, inplace=True)
olympics_df.head(10)
