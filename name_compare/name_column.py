import csv

def extract_column(input_filenames, output_filename, column_name):
    # Create a dictionary to store product data from each source
    product_data = {'Fpt': [], 'Gearvn': [], 'Phucanh': []}

    # Read the specified column from each input CSV file
    for input_filename in input_filenames:
        source = input_filename.split('_')[1]
        with open(input_filename, 'r', newline='', encoding='utf-8') as input_file:
            reader = csv.DictReader(input_file)
            column_data = [row[column_name] for row in reader]
            product_data[source] = column_data

    # Write the extracted data to the output CSV file
    with open(output_filename, 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['Fpt_Product', 'Gearvn_Product', 'Phucanh_Product'])

        # Zip the data from each source and write it to the output file row by row
        for row_data in zip(product_data['Fpt'], product_data['Gearvn'], product_data['Phucanh']):
            writer.writerow(row_data)

# Define input filenames and output filename
input_filenames = [
    './../result/qc_Fpt_result.csv', 
    './../result/qc_Gearvn_result.csv', 
    './../result/qc_Phucanh_result.csv']
output_filename = 'All_Product.csv'
column_name = 'Product'

# Extract the 'Product' column from each input CSV file and save them to the output CSV file
extract_column(input_filenames, output_filename, column_name)

print("Columns extracted and saved successfully.")
