# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


from twilio.rest import Client
from alpha_vintage import AlphaVintage

# Chave do Twillio
ACCOUNT_SID = "AC8aa391212c08e38a761de7f2292ea74c"
AUTH_TOKEN = "cd26fa2848dfd92209df51b383e55d73"


class Twilio:
    def __init__(self):
        pass

    def send_sms(self, headline: str, brief: str, url: str):
        stock = AlphaVintage()
        variation = AlphaVintage().get_variation_last_two_closing_days()
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages \
            .create(
                body=f"{stock.STOCK}: {stock.up_down}{round(variation, 2)}%"
                     f"\nHeadline: {headline}"
                     f"\nBrief: {brief}"
                     f"\n{url}",
                from_="+16197366053",
                to="+5511974880000")
        print(message.status)


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
