import json
import csv
from bs4 import BeautifulSoup

input_file = 'fpt_products.json'
output_file = 'result/fpt_result_2.csv'
shop = 'fpt'

# Open the output CSV file in write mode
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write the header row
    csv_writer.writerow(['Product', 'Url', 'Img', 'Shop', 'Price', 'Old Price', 'Status', 'Specs'])



    with open(input_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)
        products = data['datas']['filterModel']['listDefault']['list']

        for product in products:

            product_id = product['id']

            product_name = product['name']
            price = product['productVariant']['priceOnline']
            old_price = product['productVariant']['priceMarket']
            product_url = 'https://fptshop.com.vn/may-tinh-xach-tay/' + product['nameAscii']
            stock = product['productVariant']['stockQuantity']
            if stock != 0:
                status = 'có hàng'
            else:
                status = 'không có sẵn'
            img_url = 'https://images.fpt.shop/unsafe/fit-in/filters:quality(90):fill(white):upscale()/fptshop.com.vn/Uploads/Originals/' + product['urlPicture']
            specs_dict = {}
            specs = data['datas']['filterModel']['attributeSpecItems']
            for spec in specs:
                if spec['productID'] == product_id:
            
                    label = spec['attributeName']
                    value = spec['specName']
                    specs_dict[label] = value
            specs_string = "|| ".join([f"{label}: {value}" for label, value in specs_dict.items()])

            csv_writer.writerow([product_name, product_url, img_url, shop, price, old_price, status, specs_string])

print("CSV file has been created successfully!")
