from bs4 import BeautifulSoup
import requests


class Bs4Scrape:
    def __init__(self):
        self.header = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/91.0.4472.77 Safari/537.36",
                "Accept-Language": "pt-br"
            }

    def get_data_from_html(self, url: str):
        response = requests.get(url=url, headers=self.header)
        webpage = response.text
        soup = BeautifulSoup(webpage, "html.parser")
        all_link_elements = soup.select(".list-card-top a")
        print(all_link_elements)
        all_links = []
        for link in all_link_elements:
            # print(link)
            href = link["href"]
            print(href)
            if "http" not in href:
                all_links.append(f"https://www.zillow.com{href}")
            else:
                all_links.append(href)

        all_address_elements = soup.select(".list-card-info address")
        all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

        all_price_elements = soup.select(".list-card-heading")
        all_prices = []
        for element in all_price_elements:
            # Get the prices. Single and multiple listings have different tag & class structures
            try:
                # Price with only one listing
                price = element.select(".list-card-price")[0].contents[0]
            except IndexError:
                print('Multiple listings for the card')
                # Price with multiple listings
                price = element.select(".list-card-details li")[0].contents[0]
            finally:
                all_prices.append(price)
