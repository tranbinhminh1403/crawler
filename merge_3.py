import pandas as pd

# Load the CSV file into a dataframe
gearvn_df = pd.read_csv('result/qc_Gearvn_result_17_05.csv')

# Add the 'Shop' column with all values as 'gearvn'
gearvn_df['Shop'] = 'gearvn'

# Reorder the columns, assuming the original columns are ['Product', 'Product Url', 'Img', 'Price', 'Old Price', 'Specs']
gearvn_df = gearvn_df[['Product', 'Img', 'Product Url', 'Shop', 'Price', 'Old Price', 'Specs']]

# Save the modified dataframe to a new CSV file
gearvn_df.to_csv('gearvn_result.csv', index=False)

print("Data has been processed and saved to gearvn_result.csv")
