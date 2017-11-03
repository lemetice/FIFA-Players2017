# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 06:51:50 2017

@author: Arnold
"""

"""Scraping data from FIFA website"""

"""Import useful libraries"""

from bs4 import BeautifulSoup
import urllib
import requests
import pandas as pd

url = "https://www.fifaindex.com"

#Grap the page
page = requests.get(url);

html = page.content

#Grap the table containing the data
soup = BeautifulSoup(html,'lxml')
right_table = soup.find('table', class_='table table-striped players')

Name=[]
Player_url=[]
Nationality=[]
Age=[]
Prefered_position=[]
Team=[]
Hits=[]

for row in right_table.findAll("tr"):
    cells = row.find("td")
    if(cells!=None):
        Hits.append(["hits"])
        Age.append(["age"])
        
        a = cells.find("a")
            
        if(a!=None):
            Name.append(a["title"])
            Player_url.append(a["href"])
            Nationality.append(a["nationality"])
            Prefered_position.append(a["position"])
            Team.append(a["team"])
        
temp_df=pd.DataFrame({
                'Name':Name, 
                'Url' :Player_url, 
                'Nationality': Nationality,
                'Age': Age,
                'Prefered_position': Prefered_position,
                'Team': Team,
                'Hits': Hits
                })
print(temp_df)

for i in range(2,588):
    print(i)
    url_temp = url+'/players/'+str(i)+'/'
    while(True):
        print("Getting page"+str(i))
        try:
            page = requests.get(url_temp)
        except requests.exceptions.RequestException as e:
            print(e)
            continue
        break
    
    html = page.content
    soup = BeautifulSoup(html, 'lxml')
    right_table=soup.find('table', class_='table table-striped players')
    
    for row in right_table.findAll("tr"):
        cells = row.find("td")
        if(cells!=None):
            a = cells.find("a")
            if(a!=None):
                A.append(a["title"])
                B.append(a["href"])
    df =pd.DataFrame({'Name':A, 'url':B})
    print(df)
    
df.to_csv('Names.csv', index=False, encoding='utf-8')