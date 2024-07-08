import csv
import re

def clean_product_name(product_name):
    # Remove "Laptop" and "Máy tính xách tay" from the product name
    product_name = product_name.replace('Laptop', '').replace('Máy tính xách tay', '')
    
    # Remove any string inside parentheses and the parentheses themselves
    product_name = re.sub(r'\(.*?\)', '', product_name)
    
    # Remove double quotes
    product_name = product_name.replace('"', '')

    # Remove everything after the first comma (including the comma)
    if ',' in product_name:
        product_name = product_name.split(',')[0]
    
    # Remove leading and trailing whitespace
    product_name = product_name.strip()
    
    return product_name


def process_csv(input_filename, output_filename):
    # Open the input CSV file and read its contents
    with open(input_filename, 'r', newline='', encoding='utf-8') as input_file:
        reader = csv.DictReader(input_file)
        
        # Extract the 'Product' column from the input file
        products = [row['Product'] for row in reader]
    
    # Process each product name
    cleaned_products = [clean_product_name(product) for product in products]
    
    # Write the modified data to a new CSV file
    with open(output_filename, 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['Product'])  # Write header
        writer.writerows([[product] for product in cleaned_products])  # Write cleaned products

# Process the CSV file and save the cleaned data to a new file
input_filenames = [
    './../result/qc_Fpt_result.csv',
    './../result/qc_Gearvn_result.csv', 
    './../result/qc_Phucanh_result.csv'
]

output_filenames = [
    './../validated_result/Fpt_validated.csv',
    './../validated_result/Gearvn_Validated.csv',
    './../validated_result/Phucanh_Validated.csv'
]

for input_filename, output_filename in zip(input_filenames, output_filenames):
    process_csv(input_filename, output_filename)


print("Data has been cleaned and saved successfully.")
