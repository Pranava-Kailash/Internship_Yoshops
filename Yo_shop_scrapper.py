#Importing the libraries
from urllib import response
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

#Creating a List
name_list = []
name_img_list = []
url_img_list = []
cat_list = []
base_url = 'www.yoshops.com'

#Creating the product_link_list
response = urllib.request.urlopen('https://yoshops.com')
res = response.read()
soup = BeautifulSoup(res,'lxml')
test_list = soup.find_all('ul', class_ = 'nav category-bar')
for t_l in test_list:
    a = t_l.find_all('li', class_ = 'dropdown')
    for l in a:
        name_list.append(l.a['href']) 

#Creating the Webscrapper 
for product in name_list:
    print(f'Scrapping From {product}')
    response = urllib.request.urlopen(f'https://yoshops.com{product}')
    url = response.read()
    soup_2  = BeautifulSoup(url,'lxml')
    product_list = soup_2.find_all('a', class_ = 'product-link')
    for p_i in product_list:
        if p_i.find_all('img') == p_i.find_all('img',{'src':"//onlinestore.wsimg.com/assets/noimage/product-5fec99477aebb10bac85d82665ec1497de4536cda3279e59089555c45cf589fa.png"}):
            name_img_list.append(p_i.img['alt'])   
            url_img_list.append(f'{base_url}'+p_i['href'])


#Printng out the Scrapped values
num = 0
ind = -1
for name in name_img_list:
    num += 1
    ind += 1
    print(f'{num} Product Name - {name} --- Url Link - {url_img_list[ind]}')
print(f'Products without Images {num}')

#Exporting the Scapper Values to CSV
dict = {'Product Name': name_img_list, 'Url' : url_img_list}
df = pd.DataFrame(dict)
df.to_csv('Output_No_img.csv')
print('Output Has be Exported to CSV')