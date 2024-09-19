import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://example.com/products'  # Replace with actual URL
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    products = [
        {
            'Product Name': p.find('h2').text.strip(),
            'Price': p.find('span', class_='price').text.strip(),
            'Rating': p.find('span', class_='rating').text.strip()
        }
        for p in soup.find_all('div', class_='product')
    ]

    pd.DataFrame(products).to_csv('products.csv', index=False)
    print("Data saved to products.csv")
else:
    print(f"Error: {response.status_code}")
