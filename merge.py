import pandas as pd

# Load the CSV files into dataframes
qc_df = pd.read_csv('result/qc_Fpt_result_17_05.csv')
img_df = pd.read_csv('fpt_img.csv')

# Print the column names of both dataframes to check
print("QC DataFrame columns:", qc_df.columns)
print("IMG DataFrame columns:", img_df.columns)

# Merge the dataframes on the 'Product Url' column
merged_df = pd.merge(qc_df, img_df, on='Product Url', how='left')

# Print the columns of the merged dataframe to check if 'Img' is included
print("Merged DataFrame columns:", merged_df.columns)

# Check the first few rows of the merged dataframe
print("First few rows of merged DataFrame:", merged_df.head())

# Add the 'Shop' column with all values as 'fpt'
merged_df['Shop'] = 'fpt'

# Reorder the columns
desired_columns = ['Product', 'Img', 'Product Url', 'Shop', 'Price', 'Old Price', 'Specs']
# Ensure all desired columns are present
missing_columns = [col for col in desired_columns if col not in merged_df.columns]
if missing_columns:
    print(f"Warning: The following columns are missing and will be filled with 'N/A': {missing_columns}")
    for col in missing_columns:
        merged_df[col] = 'N/A'

# Reorder the columns
merged_df = merged_df[desired_columns]

# Save the merged dataframe to a new CSV file
merged_df.to_csv('fpt_result.csv', index=False)

print("Data has been merged and saved to fpt_result.csv")
