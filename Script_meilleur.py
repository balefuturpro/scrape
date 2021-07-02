import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import time
from time import sleep
from random import randint
from itertools import groupby

df = pd.DataFrame()
request = 0
pages = [str(i) for i in range(1,3)]
#possible_links = bs.find_all('a',class_="post-link post-vip")
print("--------------requetage des urls---------------------")
for page in pages:
    a = 'https://deals.jumia.sn/'
    html = requests.get(a).text
    bs = BeautifulSoup(html)
    #possible_links = bs.find_all('a',class_="post-link post-vip")
    link_categorie = bs.find_all('a',class_="category-name")
    #print(link_categorie)##
    #for link in possible_links:
    #        if link.has_attr('href'):
    #            link = link.attrs['href']
    #            print(link)
    for link in link_categorie:
        if link.has_attr('href'):
            cat = link.attrs['href']
            print(cat)
            link = a + cat
            
            link = link+'?page='+page+''
            print(link)
            a = 'https://deals.jumia.sn/'
            #html = requests.get('https://deals.jumia.sn/informatique-multimedia?page=1')
            #bs = BeautifulSoup(html)
            html = requests.get(link).text
            bs = BeautifulSoup(html)
            possible_links = bs.find_all('a' ,class_="post-link post-vip")
            for link in possible_links:
               if link.has_attr('href'):
                    link = a + link.attrs['href']
                    response = get(link)
                    html_soup = BeautifulSoup(response.text, 'html.parser')
                    price = html_soup.find_all('span',class_='price')
                    price = price[0].find('span')['content']
                    price = int(float(price))
                    n = [int(''.join(group)) for key, group in groupby(iterable=link, key=lambda e: e.isdigit()) if key] 
                    id = n[len(n) - 1]
                    name = html_soup.find('dd').text
                    address = html_soup.find_all('dd')[1].find('span').text
                    date = html_soup.find('time')['datetime']
                    title = html_soup.find_all('div')[1].h1.find('span').text
                    marque = html_soup.find_all('div')[1].h3.find('span').text
                    desc = html_soup.find_all('div')[1].p.text
                    phone = int(html_soup.find_all('div',class_="phone-box show")[0].a.text)
                    print(price,'\t',id,'\t',name,'\t',address,'\t',date,'\t',title,'\t',marque,'\t',desc,'\t',phone)
                    df = df.append(pd.DataFrame({'cat':cat, 'id':id, 'price': price, 'name': name, 'address': address, 'date': date, 'title': title, 'marque': marque, 'desc':desc,'phone':phone}, index = [0]), ignore_index = True)
                    
df.to_csv('file_test.csv', index=False, encoding='utf-8')
            #bs = BeautifulSoup(html)
            #possible_links = bs.find_all('a', class_="post-link post-vip")
            #response = get(link)
            #print(response)
            #for link in BeautifulSoup(response.text, 'html.parser')
            #price = html_soup.find_all('span',)
                            
                            
                
