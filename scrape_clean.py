
# coding: utf-8

# In[1]:


import time
from time import sleep
import random
from random import randint
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from IPython.core.display import clear_output
import warnings


# In[2]:


headers = {"Accept-Language": "en-US, en;q=0.5"}
warnings.warn('Warnings Simulation')


# In[3]:


urls=["https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Main+Deck+Monster&Rarity=Common+%2f+Short+Print&newSearch=false&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Main+Deck+Monster&newSearch=false&Rarity=Super+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Main+Deck+Monster%20&newSearch=false&Rarity=Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Main+Deck+Monster&newSearch=false&Rarity=Ultra+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Main+Deck+Monster&newSearch=false&Rarity=Secret+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Main+Deck+Monster&Rarity=Ultimate+Rare&newSearch=false&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Main+Deck+Monster&newSearch=false&Rarity=Starfoil+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Main+Deck+Monster&newSearch=false&Rarity=Gold+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Main+Deck+Monster&newSearch=false&Rarity=Mosaic+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Main+Deck+Monster&newSearch=false&Rarity=Gold+Secret+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Main+Deck+Monster&newSearch=false&Rarity=Shatterfoil+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Main+Deck+Monster&newSearch=false&Rarity=Prismatic+Secret+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Main+Deck+Monster&newSearch=false&Rarity=Ghost+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Main+Deck+Monster&newSearch=false&Rarity=Parallel+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Main+Deck+Monster&newSearch=false&Rarity=Platinum+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Main+Deck+Monster&newSearch=false&Rarity=Short+Print&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Main+Deck+Monster&newSearch=false&Rarity=Promo&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Main+Deck+Monster&newSearch=false&Rarity=Ghost%2fGold+Rare&orientation=list","https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Spell&Rarity=Common+%2f+Short+Print&newSearch=false&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Spell&newSearch=false&Rarity=Super+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Spell%20&newSearch=false&Rarity=Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Spell&newSearch=false&Rarity=Ultra+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Spell&newSearch=false&Rarity=Secret+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Spell&Rarity=Ultimate+Rare&newSearch=false&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Spell&newSearch=false&Rarity=Starfoil+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Spell&newSearch=false&Rarity=Gold+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Spell&newSearch=false&Rarity=Mosaic+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Spell&newSearch=false&Rarity=Gold+Secret+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Spell&newSearch=false&Rarity=Shatterfoil+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Spell&newSearch=false&Rarity=Prismatic+Secret+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Spell&newSearch=false&Rarity=Ghost+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Spell&newSearch=false&Rarity=Parallel+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Spell&newSearch=false&Rarity=Platinum+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Spell&newSearch=false&Rarity=Short+Print&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Spell&newSearch=false&Rarity=Promo&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Spell&newSearch=false&Rarity=Ghost%2fGold+Rare&orientation=list","https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Trap&Rarity=Common+%2f+Short+Print&newSearch=false&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Trap&newSearch=false&Rarity=Super+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Trap%20&newSearch=false&Rarity=Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Trap&newSearch=false&Rarity=Ultra+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Trap&newSearch=false&Rarity=Secret+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Trap&Rarity=Ultimate+Rare&newSearch=false&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Trap&newSearch=false&Rarity=Starfoil+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Trap&newSearch=false&Rarity=Gold+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Trap&newSearch=false&Rarity=Mosaic+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Trap&newSearch=false&Rarity=Gold+Secret+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Trap&newSearch=false&Rarity=Shatterfoil+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Trap&newSearch=false&Rarity=Prismatic+Secret+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Trap&newSearch=false&Rarity=Ghost+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Trap&newSearch=false&Rarity=Parallel+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Trap&newSearch=false&Rarity=Platinum+Rare&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Trap&newSearch=false&Rarity=Short+Print&orientation=list",
"https://shop.tcgplayer.com/yugioh/product/show?advancedSearch=true&Price_Condition=Less+Than&Type=Cards&Card+Type=Trap&newSearch=false&Rarity=Ghost%2fGold+Rare&orientation=list"]


# In[4]:


# Declare the lists to store data in
names=[]
setNumbers=[]
prices=[]

# Preparing the monitoring of the loop
start_time = time.time()
requests = 0

# For every URL 

for url in urls:
    
# Select all page link data
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    pageNum = html_soup.find_all('a', class_ = 'page-link')
    
    # Transform data type to str
    pageNum_str = str(pageNum)

    # Splice str to grab section with page number
    pageStr = pageNum_str[-20:-5]

    # Remove all non-numeric characters from splice
    pageStr = ''.join(c for c in pageStr if c.isnumeric())

    # Check if int is '', if not set to number parsed
    if pageStr == "":
        pageStr = '1'
        pageint = int(pageStr)
    else:
        pageint = int(pageStr)

    # Create range for scraper to parse for each url
    pages = [str(i) for i in range (1, pageint + 1)]

    # For every page in the interval 1-10
    for page in pages:
    
        # Make a get request
        response = get( url + '&PageNumber=' + page, headers = headers)
    
        # Pause the Loop
        sleep(randint(10,12))
    
        # Monitor the requests
        requests += 1
        elapsed_time=time.time() - start_time
        print('Request: {}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
        clear_output(wait = True)
    
        # Throw a warning for non-200 status codes
        if response.status_code != 200:
            warn('Request:{}; Status code: {}'.format(requests, response.status_code))
        
        # Break the loop if the number of requests is greater than expected
        if requests > 3000:
            warn('Number of requests was greater than expected.')
            break
        
        # Parse the content of the request with BeautifulSoup
        page_html = BeautifulSoup(response.text, 'html.parser')
    
        # Select all 10 of the card containers from a single page
        pd_containers = page_html.find_all('div', class_ = 'product')
    
        # For every card of these 10
        for container in pd_containers:
        
             # If the card has no setNumber, then:
            if container.find('span', class_ = 'product__extended-field') is not None:
           
                # Scrape the name
                name=container.find('a',class_='product__name').text
                names.append(name)
           
                # Scrape the price
                price=container.dl.dd.text
                prices.append(price)
            
                # Scrape the setNumber
                setNumber=container.find('span', class_='product__extended-field').text
                setNumbers.append(setNumber)


# In[5]:


df= pd.DataFrame ({
    'name': names,
    'setNumber': setNumbers,
    'price': prices,
})

df.to_csv('file1.csv')

import MySQLdb
import csv

db = MySQLdb.connect(user = 'tier1marketspace',
                    password = 'poopypants',
                    host = 'tier1marketspace.mysql.pythonanywhere-services.com',
                    database = 'tier1marketspace$Tier1',
                    autocommit = True,
                    local_infile = 1)
print("Connection to DB Established")

cursor = db.cursor() 
Query = "LOAD DATA LOCAL INFILE 'file1.csv' INTO TABLE Prices FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 LINES (@dummy, CardName, CardID, Price, PriceDate);"

cursor.execute(Query)
cursor.close()
db.close()
print("Connection to DB Closed")

