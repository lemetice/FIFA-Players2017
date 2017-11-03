# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""Scraping data from FIFA website"""

"""Import useful libraries"""

from bs4 import BeautifulSoup
import urllib
import requests
import pandas as pd
import shutil
import os, os.path

df = pd.read_csv("Names.csv")

print("CSV file read completely")

url = "https://www.fifaindex.com"

for i in range(1100):
    
    print(i)
    url_temp = url+df['url'][i]
    
    while(True):
        print("Getting page for "+ df['Name'][i])
        try:
            page = requests.get(url_temp)
            
        except requests.exceptions.RequestException as e: #follow the syntax below
            print(e)
            continue
        
        break
    
    html = page.content
    soup = BeautifulSoup(html, 'lxml')
    
    Nat = soup.find('img')
    print(Nat['src'])
    
    while(True):
        try:
            response = requests.get(url+Nat['src'], stream=True)
        except requests.exceptions.RequestException as e: #follow the syntax below
            print(e)
            continue
        
        break
    
    with open("Pictures/"+df['Name'][i]+".png", 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
        
    del response# -*- coding: utf-8 -*-

