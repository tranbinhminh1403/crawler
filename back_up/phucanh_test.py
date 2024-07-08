import requests
from bs4 import BeautifulSoup
import math
import csv
import re

url = "https://www.phucanh.vn/laptop-asus-expertbook-b5302cea-kg0749w.html"


product_access = requests.get(url)
product_soup = BeautifulSoup(product_access.content, "html.parser")

specs = product_soup.find(attrs={'class':"tb-product-spec"})

print(specs)