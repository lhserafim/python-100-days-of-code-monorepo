# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

import requests
from twilio_api import Twilio

NEWS_API_KEY = "81fffca69e5c4514a85c224520505865"


class News:
    def __init__(self):
        pass

    def get_news(self):
        parameters = {
            "q": "tesla",
            "from": "2021-04-29",
            "sortBy": "publishedAt",
            "apiKey": NEWS_API_KEY
        }

        response = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
        response.raise_for_status()

        # Slice in Python
        # a[start:stop]  # items start through stop-1
        # a[start:]      # items start through the rest of the array
        # a[:stop]       # items from the beginning through stop-1
        # a[:]           # a copy of the whole array

        print(response.json()["articles"][:3])
        news_list = response.json()["articles"][:3]
        for news in news_list:
            headline = news["title"]
            brief = news["description"]
            url = news["url"]
            twilio = Twilio()
            twilio.send_sms(headline=headline, brief=brief, url=url)
            print(headline, brief)



