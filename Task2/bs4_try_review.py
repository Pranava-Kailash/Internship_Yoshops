import urllib.request
from urllib import response
from bs4 import BeautifulSoup
import pandas as pd

item = []
for page in range(1,12):
    url = f'https://yoshops.com/products?page={page}'
    response_ = urllib.request.urlopen(url)
    Html = BeautifulSoup(response_.content,features='lxml')
    item = []
    for item in Html.find_all("a","product-link"):

        try:
            reviews_count = int(
                item.find(
                    "span",
                    "nav-tab-sum yotpo-reviews-nav-tab-sum",
                )
                .text.split("(")[1]
                .split(")")[0]
                .replace(" ","")
            )
        except:
            print(item)
            reviews_count = None
        
        print(reviews_count)
        # if reviews_count:
        #     item_html = BeautifulSoup(requests.get(item.attrs['href']).content,features='lxml')
        #     for review in item_html.find_all(
                
        #     )
            