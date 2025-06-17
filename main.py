import requests

# Define the URL
url = "https://api.financialdatasets.ai/prices/"
params = {
    "ticker": "AAPL",
    "interval": "day",
    "interval_multiplier": 1,
    "start_date": "2025-06-01",
    "end_date": "2025-06-10"
}

try:
    # Send GET request
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise exception for HTTP errors

    # Print the JSON response
    data = response.json()
    print(data)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
