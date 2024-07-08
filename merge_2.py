import pandas as pd
import re

# Load the CSV file into a dataframe
phucanh_df = pd.read_csv('result/qc_Phucanh_result_17_05.csv')

# Add the 'Shop' column with all values as 'phucanh'
phucanh_df['Shop'] = 'phucanh'

# Function to extract the content between the first pair of parentheses
def extract_specs(product):
    match = re.search(r'\(([^)]+)\)', product)
    return match.group(1) if match else ''

# Apply the function to the 'Product' column to create the 'Specs' column
phucanh_df['Specs'] = phucanh_df['Product'].apply(extract_specs)

# Reorder the columns
phucanh_df = phucanh_df[['Product', 'Img', 'Product Url', 'Shop', 'Price', 'Old Price', 'Specs', 'Status']]

# Save the modified dataframe to a new CSV file
phucanh_df.to_csv('phucanh_result.csv', index=False)

print("Data has been processed and saved to phucanh_result.csv")
