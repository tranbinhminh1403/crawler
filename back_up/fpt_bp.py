import requests
import json

# URL of the API endpoint
url = "https://papi.fptshop.com.vn/gw/v1/public/bff-smart-api/ai-search/product-by-category"

# Define headers (add any necessary headers for the API)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Accept": "application/json",
    # Add any other required headers here
}

# Send a GET request to the API endpoint
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON content
    data = response.json()
    
    # Write the JSON data to a file
    with open('fpt_products.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
        
    print("Data has been written to products.json")
else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
