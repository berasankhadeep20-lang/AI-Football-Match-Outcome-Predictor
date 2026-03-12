import requests

API_KEY = "5d6282fa4dmsh53bade3f9a2fe50p1c6c2fjsn039f635260bf"

URL = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"

HEADERS = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "football-prediction-api.p.rapidapi.com"
}

PARAMS = {
    "market": "classic",
    "iso_date": "2018-12-01",
    "federation": "UEFA"
}


def fetch_matches():
    response = requests.get(URL, headers=HEADERS, params=PARAMS)

    if response.status_code != 200:
        print("API Error:", response.text)
        return {}

    return response.json()