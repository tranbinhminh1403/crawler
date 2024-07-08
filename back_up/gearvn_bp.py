import requests
import json

# List of URLs to fetch data from
urls = [
    "https://gearvn.com/collections/laptop-asus-hoc-tap-va-lam-viec/products.json?include=metafields[product]&page=1&limit=50",
    "https://gearvn.com/collections/laptop-acer-hoc-tap-va-lam-viec/products.json?include=metafields[product]&page=1&limit=50",
    "https://gearvn.com/collections/laptop-msi-hoc-tap-va-lam-viec/products.json?include=metafields[product]&page=1&limit=50",
    "https://gearvn.com/collections/laptop-lenovo-hoc-tap-va-lam-viec/products.json?include=metafields[product]&page=1&limit=50",
    "https://gearvn.com/collections/laptop-dell-hoc-tap-va-lam-viec/products.json?include=metafields[product]&page=1&limit=50",
    "https://gearvn.com/collections/laptop-hp-pavilion/products.json?include=metafields[product]&page=1&limit=50",
    "https://gearvn.com/collections/laptop-lg-gram/products.json?include=metafields[product]&page=1&limit=50",
    "https://gearvn.com/collections/laptop-gaming-acer/products.json?include=metafields[product]&page=1&limit=50",
    "https://gearvn.com/collections/laptop-gaming-asus/products.json?include=metafields[product]&page=1&limit=50",
    "https://gearvn.com/collections/laptop-msi-gaming/products.json?include=metafields[product]&page=1&limit=50",
    "https://gearvn.com/collections/laptop-msi-gaming/products.json?include=metafields[product]&page=2&limit=50",
    "https://gearvn.com/collections/laptop-gaming-lenovo/products.json?include=metafields[product]&page=1&limit=50",
    "https://gearvn.com/collections/laptop-gaming-dell/products.json?include=metafields[product]&page=1&limit=50",
    "https://gearvn.com/collections/laptop-gaming-gigabyte/products.json?include=metafields[product]&page=1&limit=50",
    "https://gearvn.com/collections/laptop-gaming-hp/products.json?include=metafields[product]&page=1&limit=50"
]

# Initialize an empty list to store all products
all_products = []

# Fetch data from each URL
for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Assuming the structure is {"products": [...]}, extend the all_products list
        all_products.extend(data.get("products", []))
    else:
        print(f"Failed to retrieve data from {url}. HTTP Status code: {response.status_code}")

# Write the combined data to a single JSON file
with open('gearvn_combined_products.json', 'w', encoding='utf-8') as json_file:
    json.dump({"products": all_products}, json_file, ensure_ascii=False, indent=4)

print("Data has been written to gearvn_combined_products.json")
