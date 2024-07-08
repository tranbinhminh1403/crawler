from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
import csv

# Set Chrome options to run in headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration

# # Initialize WebDriver with Chrome options
# driver = webdriver.Chrome(options=chrome_options)

# Fetch the webpage
driver = webdriver.Chrome()
driver.get("https://fptshop.com.vn/may-tinh-xach-tay/asus-vivobook-a1405va-km059w-i5-13500h")

wait = WebDriverWait(driver, 2)

page_source = driver.page_source
driver.quit()

soup = BeautifulSoup(page_source, "html.parser")

# Find all the content within the <body> tag
# body_content = soup.find('body')

# Write the result to index.html
# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(str(body_content))

# basic info
product_name = soup.find(attrs={'class':'st-name'}).getText()

product_price = soup.find(attrs={'class':'st-price-main'}).getText()
product_old_price = soup.find(attrs={'class':'st-price-sub'}).getText()

# discount
product_discount_list = soup.find(attrs={'class':'st-boxPromo'})

# Save results into a CSV file
csv_file_path = './../result/fpt_result.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Product', 'Price', 'Old Price', 'Discount Content'])
    writer.writerow([product_name, product_price, product_old_price, product_discount_list])

print(f"Results saved to {csv_file_path}")
