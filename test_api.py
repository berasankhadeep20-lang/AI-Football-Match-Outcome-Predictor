import requests

url = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"

querystring = {
    "market": "classic",
    "iso_date": "2018-12-01",
    "federation": "UEFA"
}

headers = {
    "X-RapidAPI-Key": "5d6282fa4dmsh53bade3f9a2fe50p1c6c2fjsn039f635260bf",
    "X-RapidAPI-Host": "football-prediction-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()

print(data)