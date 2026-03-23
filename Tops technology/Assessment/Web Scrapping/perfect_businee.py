import requests                  
from bs4 import BeautifulSoup       
import pandas as pd                 

url = "http://books.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    print("Website Connected Successfully!")
else:
    print("Failed to Connect")

soup = BeautifulSoup(response.text, "html.parser") 
books = soup.find_all("article", class_="product_pod")

data = []
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    availability = book.find("p", class_="instock availability").text.strip()
    rating = book.find("p")["class"][1]
    data.append([title, price, rating, availability])

df = pd.DataFrame(data, columns=["Title", "Price", "Rating", "Availability"])

df.to_csv("books.csv", index=False)

df.to_excel("books.xlsx", index=False)

print("Data Scraped & Stored Successfully!")
print(df.head())