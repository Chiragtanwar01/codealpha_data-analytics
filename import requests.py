import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target URL
url = 'https://www.clankart.com/'

# Get page content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data
books = soup.find_all('article', class_='product_pod')

# Prepare dataset
data = []
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    availability = book.find('p', class_='instock availability').text.strip()
    data.append({'Title': title, 'Price': price, 'Availability': availability})

# Save to CSV
df = pd.DataFrame(data)
df.to_csv('booksrecord.csv', index=False)

print("Scraping complete! Dataset saved as booksrecord.csv")
