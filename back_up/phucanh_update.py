import mysql.connector
import csv

def update_products_from_csv(file_path):
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
        cursor = connection.cursor(buffered=True)

        # Open the CSV file
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Get the URL and product name from the CSV row
                csv_url = row['Url']
                csv_product_name = row['Product']

                # Check if the URL exists in the products table
                cursor.execute("SELECT product_name FROM products WHERE url = %s", (csv_url,))
                result = cursor.fetchone()

                if result:
                    # If the URL exists, update the product name in the CSV row
                    db_product_name = result[0]
                    row['Product'] = db_product_name
                    print(f"Updated product name for URL '{csv_url}' to '{db_product_name}'")

        # Close cursor and connection
        cursor.close()
        connection.close()
        print("Connection closed")

    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)

# Specify the path to the CSV file
csv_file_path = 'brand/phucanh_brand.csv'

# Call the function to update products from the CSV file
update_products_from_csv(csv_file_path)
