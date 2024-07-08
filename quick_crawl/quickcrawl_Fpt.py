from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from selenium.webdriver.chrome.options import Options
import csv

# Set Chrome options to run in headless mode
chrome_options = Options()
chrome_options.add_argument('--headless=new')  # Run Chrome in headless mode
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# # Initialize WebDriver with Chrome options
driver = webdriver.Chrome(options=chrome_options)

laptopPerPage = 9

# return numbers of laptop
# driver = webdriver.Chrome()
# driver.get("https://fptshop.com.vn/may-tinh-xach-tay?sort=ban-chay-nhat")

# wait = WebDriverWait(driver, 5)

# page_source = driver.page_source
# driver.quit()

# soup = BeautifulSoup(page_source, "html.parser")

# paginationTitle = soup.find(attrs={'class':'cdt-head'}).getText()
# numbersLaptop = int(''.join(filter(str.isdigit, paginationTitle)))

# numbersPage = math.ceil(numbersLaptop/laptopPerPage)

#####################################################################################################

# Fetch the webpage
# driver = webdriver.Chrome()
driver.get(f"https://fptshop.com.vn/may-tinh-xach-tay?sort=ban-chay-nhat&trang=25")

wait = WebDriverWait(driver, 10)

#getting the height of the webpage for infinite croll web page
last_height = driver.execute_script("return document.body.scrollHeight")

# Scroll down until no more content is loaded
while True:
    #scrolling once code
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    #giving time to load
    # time.sleep(3) # wait for content to load
    
    #checking new height of webpage
    new_height = driver.execute_script("return document.body.scrollHeight")
    
    #defining the break condition to stop the execution at the end of the webpage
    if new_height == last_height:
        break
    last_height = new_height         #while loop breaks when the last height of web page will not change

page_source = driver.page_source
driver.quit()

soup = BeautifulSoup(page_source, "html.parser")

laptop_list_container = soup.find(attrs={'class':'cdt-product-wrapper'})
laptop_list = laptop_list_container.findAll(attrs={'class':'cdt-product'})

# list_len = len(laptop_list)


with open('./../result/qc_Fpt_result_17_05.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Product', 'Product Url', 'Price', 'Old Price', 'Specs'])

    # Loop through each laptop item in laptop_list
    for laptop in laptop_list:
        product_name_tag = laptop.find(attrs={'class': 'cdt-product__name'})
        product_url = 'https://fptshop.com.vn' + product_name_tag['href']
        product_name = product_name_tag.getText()


        product_img_container = laptop.find(attrs={'class':'cdt-product__img'})

        product_img_a = product_img_container.find('a')
        product_img =  product_img_a.find('img')

        # product_img_src = product_img['src']

        if 'src' in product_img_container.attrs:
            product_img =  product_img_a.find('img')
            product_img_src = product_img['src']
        elif 'data-src' in product_img_container.attrs:
            product_img =  product_img_a.find('span')
            product_img_src = product_img['data-src']
        elif 'data-lazy-src' in product_img_container.attrs:
            product_img =  product_img_a.find('span')
            product_img_src = product_img['data-lazy-src']
        else:
            product_img_src = None

        # Try finding the price using the 'progress' class first
        product_price_elem = laptop.find(attrs={'class': 'progress'})
        if product_price_elem:
            product_price = product_price_elem.getText()
        else:
            # If 'progress' class is not found, try finding the price using the 'price' class
            product_price_elem = laptop.find(attrs={'class': 'price'})
            if product_price_elem:
                product_price = product_price_elem.getText()
            else:
                product_price = None

        # Find the old price if available
        product_old_price_strike = laptop.find(attrs={'class': 'strike-price'})
        if product_old_price_strike:
            product_old_price = product_old_price_strike.find('strike').getText()
        else:
            product_old_price = "none"
        specs_list = laptop.find(attrs={'class':'cdt-product__config__param'})
        if specs_list:
            specs = specs_list
        else:
            specs = 'none'

        # Write the extracted information to the CSV file
        writer.writerow([product_name, product_url, product_price, product_old_price, specs])

print("Data has been written to qc_Fpt_result.csv")
