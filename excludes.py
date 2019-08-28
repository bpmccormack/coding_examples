# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 14:41:31 2019

@author: bryanmccormack
"""

import pandas as pd

data = pd.read_excel(r'C:\Users\bryanmccormack\Downloads\61_NEEDS_REVIEWS_8.27.19.xlsx')
data = data.astype(str)
df = pd.DataFrame(data, columns=['Date Added','Track','Asin','Title'])

excludes = ['chainsaw','pail','leaf blower','HYOUJIN','brush','dryer','genie','Genuine Joe','backpack',
                             'curling iron','dog','cat','wig','animal','dryer',':','tea', 'Adidas', 'Fila',
                             'Reebok','Puma','Nike','basket','extension','extensions','batteries','battery','[EXPLICIT]']
my_excludes = [set(key_word.lower().split()) for key_word in excludes]
match_titles = [e for e in df.Title if any(keywords.issubset for keywords in my_excludes)]

def is_match(title, excludes = ['chainsaw','pail','leaf blower','HYOUJIN','brush','dryer','genie','Genuine Joe','backpack',
                             'curling iron','dog','cat','wig','animal','dryer',':','tea', 'Adidas', 'Fila',
                             'Reebok','Puma','Nike','basket','extension','extensions','batteries','battery','[EXPLICIT]']):
    my_excludes = [set(key_word.lower().split()) for key_word in excludes]
    if any(keywords.issubset(title.lower().split()) for keywords in my_excludes):
        return True
    return False
df['match_titles'] = df['Title'].apply(is_match)
result = df[df['match_titles']]['Asin']

def is_match(title, excludes = ['chainsaw','pail','leaf blower','HYOUJIN','brush','dryer','genie','Genuine Joe','backpack',
                             'curling iron','dog','cat','wig','animal','dryer',':','tea', 'Adidas', 'Fila',
                             'Reebok','Puma','Nike','basket','extension','extensions','batteries','battery','[EXPLICIT]']):
    my_excludes = [set(key_word.lower().split()) for key_word in excludes]
    if any(keywords.issubset(title.lower().split()) for keywords in my_excludes):
        return True
    return False
df['match_titles'] = df['Title'].apply(is_match)
results = df[df['match_titles']]['Track']

df.to_csv('Asin_List(8.28.19).csv',index=False)
