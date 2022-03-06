#Importing Necessary library
from idna import valid_contextj
import pandas as pd
from urllib import response
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import urllib.request
from tqdm import tqdm
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
item = []
for pg in range(1,12):
    URL = f'https://yoshops.com/products?page={pg}'
    browser.get(URL)
    print(f"Page {pg}")

    PATH_1 = "/html/body/div[2]/div[2]/div[2]/div/div/div"
    item = browser.find_element(By.XPATH, value = PATH_1)
    #end_product = len(item)

    for product in range(0,12):
        print(f'Scrapping {product}')

        # try:
        #     item[product].find_element(By.TAG_NAME,value = 'span').text
        #     print(item)
        # except:
        #     print('Product Link Not Found')
    #     windows = browser.window_handles
    #     browser.switch_to.window(windows[1])

    #     try:
    #         PATH_2 = '//*[@id="yotpo-reviews-27ab9262-3db2-455d-b865-463f999b9fbc"]'
    #         count = browser.find_element(By.XPATH, value= PATH_2)
    #         count = count.find_element(By.CLASS_NAME , value='total-reviews-search')
    #         PATH_3 = '//*[@id="338800541"]'
    #         for r1 in range(1,len(count)+1):
    #             dat1 = browser.find_element(By.XPATH , value= PATH_3).text
    #     except:
    #         print("No Review Found")
    # browser.close()
    # browser.switch_to.window(windows[0])

    time.sleep(2)

