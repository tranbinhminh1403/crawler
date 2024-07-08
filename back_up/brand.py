import csv

def classify_brand(product):
    # Convert product name to lowercase for case-insensitive comparison
    product_lower = product.lower()

    # List of brands and their corresponding keywords
    brands = {
        'Acer': ['acer'],
        'Asus': ['asus'],
        'Dell': ['dell'],
        'Gigabyte': ['gigabyte'],
        'HP': ['hp'],
        'Huawei': ['huawei'],
        'Lenovo': ['lenovo'],
        'LG': ['lg'],
        'Macbook': ['macbook'],
        'MSI': ['msi'],
        'VAIO': ['vaio'],
        'Masstel': ['masstel']
    }

    # Check if the product contains any brand keyword
    for brand, keywords in brands.items():
        for keyword in keywords:
            if keyword in product_lower:
                return brand
    
    # If no brand keyword is found, return 'Other'
    return 'Other'

def add_brand_column(input_filename, output_filename):
    # Read the CSV file and classify the brands
    with open(input_filename, 'r', newline='', encoding='utf-8') as input_file:
        reader = csv.DictReader(input_file)
        rows = list(reader)  # Convert reader object to list to allow multiple iterations

        # Add 'Brand' column to the header
        header = reader.fieldnames + ['Brand']

        # Classify brands for each row and add the 'Brand' column
        for row in rows:
            product = row['Product']
            brand = classify_brand(product)
            row['Brand'] = brand

    # Write the modified data to a new CSV file
    with open(output_filename, 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)

# Process each CSV file
files = [
    # {'input': 'result/fpt_result_2.csv', 'output': 'brand/fpt_brand.csv'},
    {'input': 'result/gearvn_result_2.csv', 'output': 'brand/gearvn_brand.csv'},
    {'input': 'result/phucanh_result_2.csv', 'output': 'brand/phucanh_brand.csv'}
]

for file in files:
    add_brand_column(file['input'], file['output'])

print("Brand classification completed.")
