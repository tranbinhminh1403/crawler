import pandas as pd
import re

# Function to clean the Specs column
def clean_specs(specs):
    if isinstance(specs, str):
        return re.sub(r'""', '"', specs)
    else:
        return specs

# Function to convert price to integer
def convert_price(price):
    if pd.isna(price):
        return -1
    elif price == 'none':
        return 0
    elif isinstance(price, str):
        price = price.replace('.', '').replace('₫', '').strip()
        if price.isdigit():
            return int(price)
        else:
            return -1
    elif isinstance(price, (int, float)):
        return int(price)
    else:
        return -1

# Process the files
file_paths = ['fpt_result.csv', 'phucanh_result.csv', 'gearvn_result.csv']
for file_path in file_paths:
    df = pd.read_csv(file_path)
    
    # Clean Specs column
    df['Specs'] = df['Specs'].apply(clean_specs)
    
    # # Convert Price and Old Price columns
    # df['Price'] = df['Price'].apply(convert_price)
    # df['Old Price'] = df['Old Price'].apply(convert_price)
    
    # Save the cleaned DataFrame
    df.to_csv(file_path, index=False)

print("Processing complete for all files.")
