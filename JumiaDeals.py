#Algorithme de parcour des urls
import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame()
request = 0
pages = [str(i) for i in range(1,40)]
possible_links = bs.find_all('a',class_="post-link post-vip")
print("--------------requetage des urls---------------------")
for page in pages:
    a = 'https://deals.jumia.sn'
    html = requests.get('https://deals.jumia.sn/catalog?page='+page+'').text
    bs = BeautifulSoup(html)
    possible_links = bs.find_all('a',class_="post-link post-vip")
    for link in possible_links:
            if link.has_attr('href'):
                link = a + link.attrs['href']
                #print(link)
                request = request + 1
                print(" execution de la requete ", request)
                response = get(link)
                html_soup = BeautifulSoup(response.text, 'html.parser')
                price = html_soup.find_all('span',class_='price')
                price = price[0].find('span')['content']
                price = int(float(price))
                #print(price)
                name = html_soup.find('dd').text
                #print(name)
                address = html_soup.find_all('dd')[1].find('span').text
                #print(address)
                date = html_soup.find('time')['datetime']
                #print(date)
                title = html_soup.find_all('div')[1].h1.find('span').text
                #print(title)
                marque = html_soup.find_all('div')[1].h3.find('span').text
                #print(marque)
                desc = html_soup.find_all('div')[1].p.text
                #print(desc)
                phone = int(html_soup.find_all('div',class_="phone-box show")[0].a.text)
                #print(phone)
                df = df.append(pd.DataFrame({'price': price, 'name': name, 'address': address, 'date': date, 'title': title, 'marque': marque, 'desc':desc,'phone':phone}, index = [0]), ignore_index = True)
