import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.mercadolibre.com.mx/")

soup = BeautifulSoup(response.content)

items = soup.find_all("div", {"class": "ui-item__content"})

content = list()

for item in items:
    price_tag = item.find("span", {"class": "price-tag-fraction"})
    formatted_price = price_tag.text.replace(',', '')
    name = item.find("p", {"class": "ui-item__title"}).text
    content.append({
        "price": float(formatted_price),
        "name": name,
    })

print(content)
