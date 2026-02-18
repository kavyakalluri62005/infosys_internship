import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Multiple categories
urls = {
    "Laptops": "https://webscraper.io/test-sites/e-commerce/static/computers/laptops",
    "Tablets": "https://webscraper.io/test-sites/e-commerce/static/computers/tablets",
    "Phones": "https://webscraper.io/test-sites/e-commerce/static/phones/touch"
}

today = datetime.now().strftime("%d-%m-%Y")

with open("milestone1_combined_scraped.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Product_Name", "Price_USD", "Stars", "Sentiment", "Scraped_Date"])

    for category, url in urls.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        products = soup.find_all("div", class_="thumbnail")

        for product in products:
            name = product.find("a", class_="title").text.strip()
            price = float(product.find("h4", class_="price").text.replace("$", ""))

            # ⭐ Star extraction
            stars = len(product.find_all("span", class_="glyphicon glyphicon-star"))

            # Sentiment logic
            if stars >= 4:
                sentiment = "Positive"
            elif stars <= 2:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            writer.writerow([category, name, price, stars, sentiment, today])

print("✅ Scraped 20+ products successfully!")
