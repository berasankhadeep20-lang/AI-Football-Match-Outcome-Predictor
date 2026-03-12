import requests
from datetime import date

API_KEY = "5d6282fa4dmsh53bade3f9a2fe50p1c6c2fjsn039f635260bf"

URL = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"

HEADERS = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "football-prediction-api.p.rapidapi.com"
}

def fetch_today_matches():

    today = date.today().isoformat()

    params = {
        "market": "classic",
        "iso_date": today,
        "federation": "UEFA"
    }

    response = requests.get(URL, headers=HEADERS, params=params)

    if response.status_code != 200:
        print("API error:", response.text)
        return []

    data = response.json()

    if "data" not in data:
        return []

    return data["data"]