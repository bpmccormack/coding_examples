# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 14:41:31 2019

@author: bryanmccormack
"""

import pandas as pd

data = pd.read_excel(r'C:\Users\bryanmccormack\Downloads\asin_list.xlsx')
df = pd.DataFrame(data, columns=['Track','Asin','Title'])

print (df)

excludes = ["Chainsaw", "Diaper pail", "Leaf Blower"]
my_excludes = [set(key_word.lower().split()) for key_word in excludes]
match_titles = [e for e in df.Title if any(keywords.issubset(e.lower().split()) for keywords in my_excludes)]

print(match_titles)

def is_match(title, excludes=["Chainsaw", "Diaper pail", "Leaf Blower"]):
    my_excludes = [set(key_word.lower().split()) for key_word in excludes]
    if any(keywords.issubset(title.lower().split()) for keywords in my_excludes):
        return True
    return False
df['match_titles'] = df['Title'].apply(is_match)
result = df[df['match_titles']]['Asin']

print(result)

def is_match(title, excludes=["Chainsaw", "Diaper pail", "Leaf Blower"]):
    my_excludes = [set(key_word.lower().split()) for key_word in excludes]
    if any(keywords.issubset(title.lower().split()) for keywords in my_excludes):
        return True
    return False
df['match_titles'] = df['Title'].apply(is_match)
results = df[df['match_titles']]['Track']

print(results)

results.replace('BRYAN','Z-EXCLUDE')

df.to_csv('EXCLUDES.csv',index=False)