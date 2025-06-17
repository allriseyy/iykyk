import requests
import sys
import questionary
import datetime
from tabulate import tabulate


choice = questionary.select(
    "Which stock ticker would you like to analyze?",
    choices=["AAPL", "GOOGL", "MSFT", "NVDA", "TSLA"]
).ask()

time_interval = questionary.select(
    "What time interval would you like to use?",
    choices=["second", "minute", "day", "week", "month", "year"]
).ask()

day_interval = input("What time interval would you like to use? ")

end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=int(day_interval))
start_date = start_date.strftime("%Y-%m-%d")
end_date = end_date.strftime("%Y-%m-%d")

url = "https://api.financialdatasets.ai/prices/"
params = {
    "ticker": {choice},
    "interval": {time_interval},
    "interval_multiplier": 1,
    "start_date": start_date,
    "end_date": end_date
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    rows = []
    for candle in data.get("prices", []):
        # Parse the ISO-8601 timestamp and display local date-time (UK = Europe/London)
        iso  = candle["time"].replace("Z", "+00:00")        # add UTC offset
        dt_  = datetime.datetime.fromisoformat(iso).astimezone()  # convert to local tz
        time_str = dt_.strftime("%Y-%m-%d %H:%M")           # e.g. 2025-06-17 05:00

        rows.append(
            [
                time_str,
                f"{candle['open']:.2f}",
                f"{candle['close']:.2f}",
                f"{candle['high']:.2f}",
                f"{candle['low']:.2f}",
                f"{candle['volume']:,}",
            ]
        )

    headers = ["Time (local)", "Open", "Close", "High", "Low", "Volume"]
    print()
    print(tabulate(rows, headers=headers, tablefmt="grid"))

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
