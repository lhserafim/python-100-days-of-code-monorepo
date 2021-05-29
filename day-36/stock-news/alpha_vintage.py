# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

import requests
import datetime

ALPHA_VANTAGE_API_KEY = "YI2DRPN4VWI1Z7I4"


class AlphaVintage:
    def __init__(self):
        self.STOCK = "TSLA"
        self.COMPANY_NAME = "Tesla Inc"
        self.up_down = ""

    def get_time_series_daily_adjusted(self):
        parameters = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": self.STOCK,
            "apikey": ALPHA_VANTAGE_API_KEY
        }

        response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
        response.raise_for_status()
        return response

    def get_variation_last_two_closing_days(self):
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        day_before_yesterday = today - datetime.timedelta(days=2)

        vf = float(self.get_time_series_daily_adjusted().json()["Time Series (Daily)"][str(yesterday)]["4. close"])
        vi = float(self.get_time_series_daily_adjusted().json()["Time Series (Daily)"][str(day_before_yesterday)]["4. close"])
        # Variação Percentual = (VF / VI - 1) × 100
        variation = (vf / vi - 1) * 100

        if variation > 0:
            self.up_down = "🔺"
        else:
            self.up_down = "🔻"
        print(f"Valor Final: {vf} {self.up_down}. Valor Inicial: {vi}. Variação: {round(variation, 2)}")
        return variation
