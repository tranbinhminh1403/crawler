import json
import csv
from bs4 import BeautifulSoup

def clean_string(input_string):
    """
    Removes substrings 'hl_', 'spec_', '\t' and replaces commas with '||' in the input string.
    
    Args:
    input_string (str): The input string to be cleaned.
    
    Returns:
    str: The cleaned string.
    """
    substrings_to_remove = ['hl_', 'spec_', '\t']
    for substring in substrings_to_remove:
        input_string = input_string.replace(substring, '')

    cleaned_string = input_string.replace(',', '|| ')
    return cleaned_string

input_file = 'gearvn_combined_products.json'
output_file = 'result/gearvn_result_2.csv'
shop = 'gearvn'

# Open the output CSV file in write mode
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header row
    csv_writer.writerow(['Product', 'Url', 'Img', 'Shop', 'Price', 'Old Price', 'Status', 'Specs'])

    # Open the input JSON file
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)

        # Loop through each product
        for product in data['products']:
            soup = BeautifulSoup(product['body_html'], "html.parser")

            product_name = product['title']
            product_url = "https://gearvn.com/products/" + product['handle']
            img_url = product['image']['src']
            price = int(product['variants'][0]['price'])
            old_price = int(product['variants'][0]['compare_at_price'])
            status_bool = product['variants'][0]['available']
            status = "còn hàng" if status_bool else "hết hàng"

            specs = soup.find('tbody')

            specs_dict = {}
            if specs:
                specs_list = specs.findAll(attrs={'class':'row-info'})
                for spec in specs_list:
                    label = spec.findAll('td')[0].getText()
                    value = spec.findAll('td')[1].getText()
                    # print (spec.findAll('td'))

                    specs_dict[label] = value
                # Create the formatted string of specifications
                specs_string = "|| ".join([f"{label}: {value}" for label, value in specs_dict.items()])

            else:
                # specs_string = 'none'
                specs_string = clean_string(product['tags'])

            # Write the extracted data to the CSV file
            csv_writer.writerow([product_name, product_url, img_url, shop, price, old_price, status, specs_string])

print("CSV file has been created successfully!")
