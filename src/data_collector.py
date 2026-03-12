import pandas as pd

def build_dataset(api_data):

    rows = []

    matches = api_data["data"]

    for match in matches:

        result = match.get("result")

        # Skip matches without valid result
        if result is None or "-" not in result:
            continue

        try:
            home_goals = int(result.split("-")[0].strip())
            away_goals = int(result.split("-")[1].strip())
        except ValueError:
            # skip results like "postp", "canc", etc.
            continue

        rows.append({
            "home_team": match["home_team"],
            "away_team": match["away_team"],
            "competition": match["competition_name"],
            "home_goals": home_goals,
            "away_goals": away_goals,
            "prediction": match["prediction"],
            "odds_home": match["odds"]["1"],
            "odds_draw": match["odds"]["X"],
            "odds_away": match["odds"]["2"]
        })

    df = pd.DataFrame(rows)

    return df