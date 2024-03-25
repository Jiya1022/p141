
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests

# NASA Exoplanet URL
bright_stars_url = "https://en.wikipedia.org/wiki/Lists_of_stars"

page = requests.get(bright_stars_url) 
print(page)

soup = bs(page.text,'html.parser') 
star_table = soup.find('table') 
temp_list= []


# Define Exostar Data Scrapping Method
table_rows = star_table.find_all('tr')
for tr in table_rows: 
    td = tr.find_all('td') 
    row = [i.text.rstrip() for i in td] 
    temp_list.append(row)


Star_names = [] 
Distance =[] 
Mass = [] 
Radius =[] 
Lum = []
print (temp_list[2])
print(len(temp_list))
print(type(temp_list))


for i in range(1,len(temp_list)): 
    Star_names.append(temp_list[i]) 
    Distance.append(temp_list[i]) 
    Mass.append(temp_list[i]) 
    Radius.append(temp_list[i]) 
    Lum.append(temp_list[i])
    
    
df2 =pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity']) 
print(df2)
df2.to_csv('bright_stars.csv')

