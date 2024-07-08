import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options

# Set Firefox options to run in headless mode
firefox_options = Options()
firefox_options.add_argument('--headless')  # Run Firefox in headless mode
firefox_options.add_argument('--disable-gpu')  # Disable GPU acceleration
firefox_options.add_argument('--no-sandbox')
firefox_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Firefox(options=firefox_options)


def fetch_product_details(product_url):


    driver.get(product_url)

    time.sleep(5)

    page_source = driver.page_source
    driver.quit()

    soup = BeautifulSoup(page_source, "html.parser")

    # Fetch the status
    status_string = soup.find(attrs={'class': 'btn-buynow'}).getText().strip()
    if status_string != 'HẾT HÀNG':
        status = 'còn hàng'
    else:
        status = 'hết hàng'

    # Fetch the specifications
    specs = soup.find('tbody')

    # label = specs_list.findAll('td')[1]
    # print(specs_list)

    specs_dict = {}
    if specs:
        specs_list = specs.findAll(attrs={'class':'row-info'})
        for spec in specs_list:
            label = spec.findAll('td')[0].getText()
            value = spec.findAll('td')[1].getText()

            specs_dict[label] = value
        # Create the formatted string of specifications
        specs_string = "; ".join([f"{label}: {value}" for label, value in specs_dict.items()])

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

# Example usage:
product_url = "https://gearvn.com/products/laptop-lenovo-ideapad-slim-3-15abr8-82xm00ehvn"
status, specs_string = fetch_product_details(product_url)
print("Status:", status)
print("Specifications:\n", specs_string)
