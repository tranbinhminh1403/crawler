import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("https://gearvn.com/products/laptop-asus-vivobook-14-oled-a1405va-km257w")
soup = BeautifulSoup(response.content, "html.parser")

# basic info & price
product_name = soup.find(attrs={'class':'product-name'}).get_text()

product_price_container = soup.find(attrs={'class':'product-price'})
product_price = product_price_container.find('span').get_text()
product_old_price =product_price_container.find('del').get_text()

product_percent_price = soup.find('span',attrs={'class':'pro-percent'})

# gift
product_gift_container = soup.find(attrs={'class':'product-desc-short'}).getText()
# product_gift = product_discount_container.findAll('span')[1].get_text()

# discount
product_discount_list = soup.find(attrs={'class':'discount-promo--lists'})
product_discount = product_discount_list.findAll('ul')

# spec
product_spec_container = soup.find('div',attrs={'class':'product-wrap'})
product_spec_content = product_spec_container.find(attrs={'class':'desc-content'})

spec_map = product_spec_content.findAll('td')
spec_len = len(spec_map)

product_specs = {}


for i in range(0, len(spec_map), 2):
    if i < len(spec_map) - 1:
        key = spec_map[i].text.strip()
        value = spec_map[i + 1].text.strip()
        product_specs[key] = value


print(product_specs)