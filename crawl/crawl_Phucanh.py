import requests
from bs4 import BeautifulSoup
import csv

# Fetch the webpage
response = requests.get("https://www.phucanh.vn/laptop-tay-asus-vivobook-14-oled-a1405va-km095w.html")
soup = BeautifulSoup(response.content, "html.parser")

# basic info
product_name = soup.find('h1', string=lambda text: text and "Laptop" in text).getText()

product_price = soup.find(attrs={'class':'detail-product-best-price'}).getText()
product_old_price = soup.find(attrs={'class':'detail-product-old-price'}).getText()


# discount
product_discount_container = soup.find(attrs={'id': 'offerTop'})
product_discount_list = product_discount_container.find(attrs={'class':'content'})


# Save results into a CSV file
csv_file_path = './../result/phucanh_result.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Product', 'Price', 'Old Price', 'Discount Content'])
    writer.writerow([product_name, product_price, product_old_price, product_discount_list])

print(f"Results saved to {csv_file_path}")