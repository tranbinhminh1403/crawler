import requests
import pandas as pd
from bs4 import BeautifulSoup
import math
import csv
import re

baseUrl = "https://www.phucanh.vn/laptop.html?page={page}"
laptopPerPage = 30
shop = 'phucanh'

def convert_price(price):
    if pd.isna(price):
        return -1
    elif price == 'none':
        return 0
    elif isinstance(price, str):
        price = price.replace('.', '').replace('₫', '').strip()
        if price.isdigit():
            return int(price)
        else:
            return -1
    elif isinstance(price, (int, float)):
        return int(price)
    else:
        return -1

response = requests.get(baseUrl.format(page=1))
soup = BeautifulSoup(response.content, "html.parser")

paginationTitle = soup.find(attrs={'class': 'product-title-group'})
titleLine = paginationTitle.find('h2').getText()

# Change to int
numbersLaptop = int(''.join(filter(str.isdigit, titleLine)))

# Calculate number of pages
numbersPage = math.ceil(numbersLaptop / laptopPerPage)

# Open a CSV file for writing
with open('./../result/phucanh_result.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Product', 'Url', 'Img', 'Shop', 'Price', 'Old Price', 'Status', 'Specs'])

    # Loop through each page
    for page in range(1, numbersPage + 1):
        response = requests.get(baseUrl.format(page=page))
        soup = BeautifulSoup(response.content, "html.parser")


        # Extract product information from the page
        laptop_list = soup.findAll(attrs={'class': 'p-item-group'})
        for laptop in laptop_list:
            product_name = laptop.find(attrs={'class': 'p-name'}).getText()
            product_url = laptop.find(attrs={'class': 'p-img'})['href']

            product_access = requests.get("https://www.phucanh.vn" + product_url)
            product_soup = BeautifulSoup(product_access.content, "html.parser")

            specs = product_soup.find(attrs={'class':"tb-product-spec"})
            if specs:
                specs_dict = {}
                specs_list = specs.findAll('tr')
                for spec in specs_list:
                    label = spec.findAll('td')[0].getText()
                    value = spec.findAll('td')[1].getText()

                    specs_dict[label] = value

                specs_string = "|| ".join([f"{label}: {value}" for label, value in specs_dict.items()])
            else:
                specs_string = 'none'
            
            img_container = laptop.find(attrs={'class':'p-img'})
            img = laptop.find(attrs={'class':'lazy'})

            img_src = img['data-src']
            
            product_price_tags = laptop.findAll(attrs={'class': 'p-price2'})
            product_price = 'none'  # Default value
            if product_price_tags:
                if len(product_price_tags) > 1:
                    product_price = ''.join(filter(lambda x: not x.name, product_price_tags[1].contents)).strip()
                else:
                    product_price = ''.join(filter(lambda x: not x.name, product_price_tags[0].contents)).strip()
            
            product_old_price_tags = laptop.findAll(attrs={'class': 'p-oldprice2'})
            product_old_price = 'none'  # Default value
            if product_old_price_tags:
                if len(product_old_price_tags) > 1:
                    product_old_price = ''.join(filter(lambda x: not x.name, product_old_price_tags[1].contents)).strip()
                else:
                    product_old_price = ''.join(filter(lambda x: not x.name, product_old_price_tags[0].contents)).strip()
            
            product_bottom = laptop.find(attrs={'class': 'p-bottom'})
            product_status_with_symbol = product_bottom.find('span')
            if product_status_with_symbol:
                product_status_with_symbol_text = product_status_with_symbol.getText()
            else:
                product_status_with_symbol_text = 'none'

            # Remove any non-alphanumeric characters from the beginning of the string
            product_status = re.sub(r'^\W+', '', product_status_with_symbol_text).strip()

            product_price = convert_price(product_price)
            product_old_price = convert_price(product_old_price)

            # Write the extracted information to the CSV file
            writer.writerow([product_name, product_url, img_src, shop, product_price, product_old_price, product_status, specs_string])

print("Data has been written to phucanh_laptop_data.csv")
