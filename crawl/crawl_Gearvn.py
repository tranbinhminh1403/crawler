from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import csv

driver = webdriver.Chrome()
driver.get('https://gearvn.com/products/laptop-asus-vivobook-14x-oled-a1405va-km095w')
driver.implicitly_wait(10)

page_source = driver.page_source
driver.quit()

soup = BeautifulSoup(page_source, "html.parser")

# basic info & price
product_name = soup.find(attrs={'class':'product-name'}).get_text()

product_price_container = soup.find(attrs={'class':'product-price'})
product_price = product_price_container.find('span').get_text()
product_old_price =product_price_container.find('del').get_text()

product_percent_price = soup.find('span',attrs={'class':'pro-percent'})

# # gift
# product_gift_container = soup.find(attrs={'class':'product-desc-short'}).getText()
# # product_gift = product_discount_container.findAll('span')[1].get_text()

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


# print(product_discount_list)

# Save results into a CSV file
csv_file_path = './../result/gear_result.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Product', 'Price', 'Old Price', 'Discount Content'])
    writer.writerow([product_name, product_price, product_old_price, product_discount_list])

print(f"Results saved to {csv_file_path}")