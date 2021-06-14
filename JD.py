from requests import get
from bs4 import BeautifulSoup
url = "https://deals.jumia.sn/appartement-meubl-louer-au-plateau-pid9582625"
response = get(url)
html_soup = BeautifulSoup(response.text, 'html.parser')
price = html_soup.find_all('span',class_='price')
price = price[0].find('span')['content']
price = int(float(price))
price
name = html_soup.find('dd').text
name
address = html_soup.find_all('dd')[1].find('span').text
address
date = html_soup.find('time')['datetime']
date
title = html_soup.find_all('div')[1].h1.find('span').text
title
marque = html_soup.find_all('div')[1].h3.find('span').text
marque
desc = html_soup.find_all('div')[1].p.text
desc
phone = int(html_soup.find_all('div',class_="phone-box show")[0].a.text)
phone
import pandas as pd
price_= []
name_ = []
address_ =[]
date_ = []
title_ = []
marque_ = []
desc_ = []
phone_ = []

dataset_ = pd.DataFrame({
    "price_" : price,
    "name_" : name,
    "address" : address,
    "date_" :date,
    "title_" :title,
    "marque_":marque,
    "desc_" : desc,
    "phone_" : phone
}, index=[0])
dataset_.head()
