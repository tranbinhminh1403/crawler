import mysql.connector
import csv

# Function to get brand ID based on brand name
def get_brand_id(brand):
    brand_dict = {
        'Acer': 1,
        'Asus': 2,
        'Dell': 3,
        'Gigabyte': 4,
        'HP': 5,
        'Huawei': 6,
        'Lenovo': 7,
        'LG': 8,
        'Macbook': 9,
        'MSI': 10,
        'VAIO': 11,
        'Masstel': 12,
        'Other': 13
    }
    return brand_dict.get(brand, 13)  # Default to 13 if brand is not found

try:
    # Establish connection to MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1403",
        database="laptop_compare2"
    )

    if connection.is_connected():
        print("Connected to MySQL database")

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Process the files
    file_paths = ['Fpt_with_Brand.csv', 'Phucanh_with_Brand.csv', 'Gearvn_with_Brand.csv']
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Map shop names to shop IDs
                shop_name = row['Shop']
                if shop_name == 'fpt':
                    shop_id = 1
                elif shop_name == 'gearvn':
                    shop_id = 2
                elif shop_name == 'phucanh':
                    shop_id = 3

                # Get brand ID
                brand = row['Brand']
                brand_id = get_brand_id(brand)

                # Insert data into products table
                cursor.execute("INSERT INTO products (product_name, img, url, shop_id, brand_id, category_id, specs, active) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                               (row['Product'], row['Img'], row['Product Url'], shop_id, brand_id, 1, row['Specs'], True))
                
                # Get the product ID of the inserted product
                product_id = cursor.lastrowid
                
                # Insert data into history table
                cursor.execute("INSERT INTO history (product_id, price, old_price, status) VALUES (%s, %s, %s, %s)",
                               (product_id, row['Price'], row['Old Price'], row['Status']))

        connection.commit()
        print(f"Data from {file_path} inserted successfully.")

except mysql.connector.Error as e:
    print("Error connecting to MySQL database:", e)

finally:
    # Close cursor and connection
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close() 
        print("Connection closed")
