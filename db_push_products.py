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
        database="laptop_compare"
    )

    if connection.is_connected():
        print("Connected to MySQL database")

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()


    # Insert data from Fpt_with_Brand.csv
    # with open('./result1/Fpt_with_Brand.csv', 'r', newline='', encoding='utf-8') as csvfile:
    #     csv_reader = csv.DictReader(csvfile)
    #     for row in csv_reader:
    #         product_name = row['Product']
    #         url = row['Product Url']
    #         brand = row['Brand']
    #         brand_id = get_brand_id(brand)
    #         # Insert data into fpt_products table
    #         sql = "INSERT INTO fpt_products (product_name, url, brand_id) VALUES (%s, %s, %s)"
    #         values = (product_name, url, brand_id)
    #         try:
    #             cursor.execute(sql, values)
    #             connection.commit()
    #         except mysql.connector.Error as e:
    #             print(f"Error inserting product: {product_name}. {e}")
    #     print("Data from Fpt_with_Brand.csv inserted successfully into fpt_products table")

    # Insert data from Gearvn_with_Brand.csv
    with open('./result1/Gearvn_with_Brand.csv', 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            product_name = row['Product']
            url = row['Product Url']
            brand = row['Brand']
            brand_id = get_brand_id(brand)
            # Insert data into gearvn_products table
            sql = "INSERT INTO gearvn_products (product_name, url, brand_id) VALUES (%s, %s, %s)"
            values = (product_name, url, brand_id)
            try:
                cursor.execute(sql, values)
                connection.commit()
            except mysql.connector.Error as e:
                print(f"Error inserting product: {product_name}. {e}")
        print("Data from Gearvn_with_Brand.csv inserted successfully into gearvn_products table")

    # Insert data from Phucanh_with_Brand.csv
    # with open('./result1/Phucanh_with_Brand.csv', 'r', newline='', encoding='utf-8') as csvfile:
    #     csv_reader = csv.DictReader(csvfile)
    #     for row in csv_reader:
    #         product_name = row['Product']
    #         url = row['Product Url']
    #         brand = row['Brand']
    #         brand_id = get_brand_id(brand)
    #         # Insert data into phucanh_products table
    #         sql = "INSERT INTO phucanh_products (product_name, url, brand_id) VALUES (%s, %s, %s)"
    #         values = (product_name, url, brand_id)
    #         try:
    #             cursor.execute(sql, values)
    #             connection.commit()
    #         except mysql.connector.Error as e:
    #             print(f"Error inserting product: {product_name}. {e}")
    #     print("Data from Phucanh_with_Brand.csv inserted successfully into phucanh_products table")


except mysql.connector.Error as e:
    print("Error connecting to MySQL database:", e)

finally:
    # Close cursor and connection
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close() 
        print("Connection closed")
