import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options

baseUrl = "https://gearvn.com"

# URLs to scrape
urls_to_scrape = [
    'laptop-asus-hoc-tap-va-lam-viec',
    'laptop-acer-hoc-tap-va-lam-viec',
    'laptop-msi-hoc-tap-va-lam-viec',
    'laptop-lenovo-hoc-tap-va-lam-viec',
    'laptop-dell-hoc-tap-va-lam-viec',
    'laptop-hp-pavilion',
    'laptop-lg-gram',
    'laptop-gaming-acer',
    'laptop-gaming-asus',
    'laptop-msi-gaming',
    'laptop-gaming-lenovo',
    'laptop-gaming-dell',
    'laptop-gaming-gigabyte',
    'laptop-gaming-hp'
]

# Set Firefox options to run in headless mode
firefox_options = Options()
firefox_options.add_argument('--headless')  # Run Firefox in headless mode
firefox_options.add_argument('--disable-gpu')  # Disable GPU acceleration
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')

def fetch_product_details(product_url):
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(product_url)
    time.sleep(3)

    page_source = driver.page_source
    driver.quit()

    soup = BeautifulSoup(page_source, "html.parser")

    # Fetch the status
    status = soup.find(attrs={'class': 'btn-buynow'}).getText().strip()

    # Fetch the specifications
    specs = soup.find('tbody')
    # specs_list = specs.findAll(attrs={'class':'row-info'})

    specs_dict = {}
    if specs:
        specs_list = specs.findAll(attrs={'class':'row-info'})
        for spec in specs_list:
            label = spec.findAll('td')[0].getText()
            value = spec.findAll('td')[1].getText()

            specs_dict[label] = value
        # Create the formatted string of specifications
        specs_string = "|| ".join([f"{label}: {value}" for label, value in specs_dict.items()])

    else:
        # specs_string = 'none'
        specs_div = soup.find(attrs={'class':'table-technical'})
        specs_list = specs_div.findAll('li')
        for spec in specs_list:
            label = spec.findAll('div')[0].getText()
            value = spec.findAll('div')[1].getText()

            specs_dict[label] = value
        # Create the formatted string of specifications
        specs_string = "|| ".join([f"{label}: {value}" for label, value in specs_dict.items()])
        # specs_string = specs

    return status, specs_string

def scrape_laptop_data(url, writer):
    # Open Firefox WebDriver
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(f'https://gearvn.com/collections/{url}')

    # Wait for the page to load
    time.sleep(5)

    # Get the updated page source
    page_source = driver.page_source
    driver.quit()

    # Parse the updated page source with BeautifulSoup
    soup = BeautifulSoup(page_source, "html.parser")

    # Extract the updated laptop list
    laptop_list = soup.findAll(attrs={'class':'proloop'})

    # Extract product information from the laptop list
    for laptop in laptop_list:
        product_name_tag = laptop.find(attrs={'class':'proloop-name'})
        product_name = product_name_tag.getText().strip()
        product_url = baseUrl + product_name_tag.find('a')['href']
        product_old_price = laptop.find(attrs={'class':'proloop-price--compare'}).getText().strip()
        product_price = laptop.find(attrs={'class':'proloop-price--highlight'}).getText().strip()

        status, specs_string = fetch_product_details(product_url)

        img_container = laptop.find(attrs={'class':'img-default'})
        img_src = img_container['data-src']

        # Write the extracted data to the CSV file immediately
        writer.writerow([product_name, product_url, img_src, product_price, product_old_price, specs_string, status])
        print(f"Product {product_name} written to CSV")

# Open the CSV file in write mode
with open('./../result/qc_Gearvn_result_29_05.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Product', 'Product Url', 'Img', 'Price', 'Old Price', 'Specs', 'Status'])

    # Scrape data for each URL and write to the CSV file
    for url in urls_to_scrape:
        scrape_laptop_data(url, writer)
        print(f"Scrape successful: {url}")

print("Data has been written to qc_Gearvn_result.csv")
