from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from selenium.webdriver.firefox.options import Options
import csv

# Read new_fpt_product.csv
with open('new_fpt_product.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    for row in reader:
        product_url = row[1]  # Get the second column (Product Url)

        # Initialize WebDriver with Chrome options
        # chrome_options = Options()
        # chrome_options.add_argument('-headless')  # Run Chrome in headless mode
        # chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')

        firefox_options = Options()

        firefox_options.add_argument('-headless=new')  # Run Chrome in headless mode
        firefox_options.add_argument('-disable-gpu')  # Disable GPU acceleration
        firefox_options.add_argument('-no-sandbox')
        firefox_options.add_argument('-disable-dev-shm-usage')

        firefox_options.add_argument('-headless')
        driver = webdriver.Firefox(options=firefox_options)

        driver.get(product_url)

        page_source = driver.page_source
        driver.quit()

        soup = BeautifulSoup(page_source, "html.parser")

        img = soup.find(attrs={'class':'swiper-slide'})
        if img:
            img_src = img['data-src']
        else:
            img_src = ''  # Set a default value if no image is found

        # Write to fpt_img.csv
        with open('fpt_img.csv', 'a', newline='') as imgfile:
            writer = csv.writer(imgfile)
            writer.writerow([product_url, img_src])