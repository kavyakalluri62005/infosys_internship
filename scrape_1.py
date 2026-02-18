import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("div", class_="thumbnail")

with open("scraped_products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Define Schema (Column Structure)
    writer.writerow([
        "Product_Name",
        "Price_USD",
        "Stars",
        "Sentiment",
        "Scraped_Date"
    ])

    for product in products:
        # Extract product name
        name = product.find("a", class_="title").text.strip()
        
        # Extract and clean price
        price_text = product.find("h4", class_="price").text.strip()
        price = float(price_text.replace("$", ""))
        
        # Extract star rating
        rating_tag = product.find("p", {"data-rating": True})
        stars = int(rating_tag["data-rating"]) if rating_tag else 0
        
        # Define Sentiment
        if stars >= 4:
            sentiment = "Positive"
        elif stars <= 2:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        
        # Scraped date
        scraped_date = datetime.now().strftime("%Y-%m-%d")
        
        writer.writerow([name, price, stars, sentiment, scraped_date])

print("Milestone 1 Data Pipeline Completed Successfully!")
