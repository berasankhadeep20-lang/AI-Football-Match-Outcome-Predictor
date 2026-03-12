import requests
from config import API_KEY, API_HOST, BASE_URL


headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": API_HOST
}


def get_matches(league_id, season):

    url = f"{BASE_URL}/fixtures"

    params = {
        "league": league_id,
        "season": season
    }

    response = requests.get(url, headers=headers, params=params)

    return response.json()