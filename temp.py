from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import csv
from bs4 import BeautifulSoup

# Set Chrome options to run in headless mode
chrome_options = Options()
chrome_options.add_argument('--headless=new')  # Run Chrome in headless mode
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Initialize WebDriver with Chrome options
driver = webdriver.Chrome(options=chrome_options)

# Fetch the webpage
driver.get(f"https://fptshop.com.vn/may-tinh-xach-tay?sort=ban-chay-nhat&trang=25")

# Scroll down to the bottom of the page to load lazy-loaded images
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load the page
    WebDriverWait(driver, 5).until(lambda d: d.execute_script("return document.readyState") == "complete")

    # Calculate new scroll height and compare with the last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Get the page source after scrolling
page_source = driver.page_source
driver.quit()

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")
laptop_list_container = soup.find(attrs={'class': 'cdt-product-wrapper'})
laptop_list = laptop_list_container.findAll(attrs={'class': 'cdt-product'})

# Write the data to a CSV file
with open('qc_Fpt_result_16_05.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Product', 'Product Url', 'Price', 'Old Price', 'Specs'])

    # Loop through each laptop item in laptop_list
    for laptop in laptop_list:
        product_name_tag = laptop.find(attrs={'class': 'cdt-product__name'})
        product_url = 'https://fptshop.com.vn' + product_name_tag['href']
        product_name = product_name_tag.getText()

        product_img_container = laptop.find(attrs={'class': 'cdt-product__img'})
        product_img_a = product_img_container.find('a')
        product_img = product_img_a.find('img') if product_img_a else None

        # Check if the product_img is not None before accessing its attributes
        if product_img:
            if 'src' in product_img.attrs:
                product_img_src = product_img['src']
            elif 'data-src' in product_img.attrs:
                product_img_src = product_img['data-src']
            elif 'data-lazy-src' in product_img.attrs:
                product_img_src = product_img['data-lazy-src']
            else:
                product_img_src = None
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
                product_price = "none"

        # Find the old price if available
        product_old_price_strike = laptop.find(attrs={'class': 'strike-price'})
        if product_old_price_strike:
            product_old_price = product_old_price_strike.find('strike').getText()
        else:
            product_old_price = "none"
        
        specs_list = laptop.find(attrs={'class': 'cdt-product__config__param'})
        if specs_list:
            specs = specs_list.getText()
        else:
            specs = "none"

        # Write the extracted information to the CSV file
        writer.writerow([product_name, product_url, product_price, product_old_price, specs])

print("Data has been written to qc_Fpt_result_16_05.csv")
