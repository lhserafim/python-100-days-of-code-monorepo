import requests
from bs4 import BeautifulSoup
import lxml
from smtp_email import EmailManager

header = {
    "Request Line": "GET / HTTP/1.1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "Version/14.1.1 Safari/605.1.15",
    "Accept-Language": "pt-br"
}

URL = "https://www.amazon.com.br/Macbook-Apple-Retina-Radeon-Espacial/dp/B07R7S26J8/ref=sr_1_13?__mk_pt_BR=ÅM" \
      "ÅŽÕÑ&dchild=1&keywords=macbook&qid=1623106913&refinements=p_89%3AApple&rnid=18120432011&s=electronics&sr=1-13 "

BUY_PRICE = 90000

content = requests.get(url=URL, headers=header).text

soup = BeautifulSoup(content, "lxml")
price = soup.find(id="priceblock_ourprice").getText()
price_without_comma = price.replace('.', '').replace(',', '.')
price_without_currency = price_without_comma.split('R$')[1]
price_as_float = float(price_without_currency)
print(type(price_as_float))
print(price_as_float)


if price_as_float < BUY_PRICE:
    email = EmailManager()
    msg = f"Subject:Amazon Price Alert!\n\nThe product that you've been tracking is now for ONLY {price}\n."
    email.send_email("lhserafim@gmail.com", msg)

