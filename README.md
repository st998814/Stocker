# Stocker

## A widget for collecting daily stock market information

##### This friendly application allow user gather stock information by just clicking a button 

##### You can sort any stock indicator by character or volume 


### Web crawler

* Chromedrive
* web request

### Raw data arrangement

```
for da in data.split('\n'):
   if len(da.split('","')) == 16 and da.split('","')[0][0] != '=':   
       cleaned_data.append([ele.replace('",\r','').replace('"','')  
                            for ele in da.split('","')])  
```
### Store data to excel worksheet with pandas

* Data frame method
* xlwinags

### Build GUI with TKinter


