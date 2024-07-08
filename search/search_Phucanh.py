import requests
from bs4 import BeautifulSoup
import csv

baseUrl = "https://www.phucanh.vn/laptop.html?page={page}"
page = 1

response = requests.get(baseUrl)
soup = BeautifulSoup(response.content, "html.parser")

paginationTitle = soup.find(attrs={'class':'product-title-group'})
titleLine = paginationTitle.find('h2').getText()


# change to int
numbersPage = int(''.join(filter(str.isdigit, titleLine)))

print(numbersPage)