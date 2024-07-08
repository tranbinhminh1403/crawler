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
output_file = 'result/gearvn_result.csv'

with open(input_file, 'r', encoding='utf-8') as infile:
    data = json.load(infile)

    product = data['products'][53]
    soup = BeautifulSoup(product['body_html'], "html.parser")

    product_name = product['title']
    product_url = "https://gearvn.com/products/" + product['handle']
    img_url = product['image']['src']
    price = int(product['variants'][0]['price'])
    old_price = int(product['variants'][0]['compare_at_price'])
    status_bool = product['variants'][0]['available']
    if status_bool == True:
        status = "còn hàng"
    else:
        status = "hết hàng"

    specs = soup.find('tbody')
    # specs_list = specs.findAll(attrs={'class':'row-info'})

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


print(specs_string)