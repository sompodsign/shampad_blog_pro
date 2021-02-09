from bs4 import BeautifulSoup
import requests
from django.core.mail import send_mail


def track_price(url, email, expected_price):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,bn;q=0.8",
    }
    status = False
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("span", id="productTitle").getText().strip()
    try:
        price = float(soup.find("span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText()[1:])
    except AttributeError:
        price = None
    if price is not None:
        if price < float(expected_price):
            status = True
            send_mail(
                'Price Reduced',
                f'Product: {title}. Price reduced to {price}. Here is the link: {url}',
                'shampadsh@gmail.com',
                [email, ],
            )
    return title, price, status
