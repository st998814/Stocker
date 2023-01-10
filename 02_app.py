from cmath import e
from datetime import date
from importlib.resources import path
from tkinter import *
from path import Path
import requests
import pandas as pd
import os
import os.path
import xlwings as xw














#functions


def sorting_PE(arg=None):
 date = en.get()       #can get num : 0,1
 url = "https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date="+date+"&type=ALL"
 res = requests.get(url)
 data = res.text

 cleaned_data = []
 for da in data.split('\n'):       
     if len(da.split('","')) == 16  and da.split('","') [0][0] != '=' :
       cleaned_data.append([ele.replace('",\r','').replace('"','')  
                            for ele in da.split('","')])                       
 df = pd.DataFrame(cleaned_data, columns = cleaned_data[0]) 
 df = df.set_index('證券代號')[1:]



 #str to numeric
 df['本益比'] = df['本益比'].str.replace(',', '').astype(float)    #replace ",", to none for float transfer

 #sort by P/E
 output_pe = df.sort_values(['本益比'],ascending=False)


#save file to path
 Direction_path = r'C:\Users\st998\Desktop\本益比排序'


 variable_path = date
 #add file extension
 suffix = '.xlsx'

 final_path = os.path.join(Direction_path,variable_path+suffix)

 output_pe.to_excel(final_path,sheet_name="本益比")
 xw.view(output_pe)





#window setup

win = Tk()

win.title('TW Stock Generator')

win.geometry("300x200")  

win.minsize(width=300,height=200)

win.resizable(False,False)

win.iconbitmap("D:\Python\Tkinter\ms_excel.ico")

win.config(background="black")

win.attributes("-alpha",1)          #0-1  floater

win.attributes("-topmost",1)



#label  

lb = Label(bg="black",fg="red",text="Format:yyyymmdd")

lb.pack()

#entry box
en = Entry()    
en.pack()

#button
btn= Button(text='Sorting by P/E',command=sorting_PE)

btn.pack()





win.mainloop()


























