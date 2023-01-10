from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import requests
import os
import os.path
import json
import numpy as np
import pandas as pd
from io import StringIO
import xlwings as xw
import pickle
import openpyxl

#get stock data

url = "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=20220422&type=ALL"
res = requests.get(url)
data = res.text


for da in data.split('\n'):       #data.split換行,將字串轉成 list
     if len(da.split('","')) == 16  and da.split('","') [0][0] != '=' :                 
         print(da.split('","'))
 
# clean data
cleaned_data = []
for da in data.split('\n'):
   if len(da.split('","')) == 16 and da.split('","')[0][0] != '=':   
       cleaned_data.append([ele.replace('",\r','').replace('"','')  
                            for ele in da.split('","')])  


#Create excel and modified with pandas

df = pd.DataFrame(cleaned_data, columns = cleaned_data[0]) #
df = df.set_index('證券代號')[1:]


df['本益比'] = df['本益比'].str.replace(',', '').astype(float)


output_pe = df.sort_values(['本益比'],ascending=False)

output_pe.to_excel('本益比排序.xlsx',sheet_name='本益比排序')

xw.view(output_pe)
































