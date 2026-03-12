def predict_today_matches(matches, model, feature_builder):

    predictions = []

    for match in matches:

        home = match["home_team"]
        away = match["away_team"]

        features = feature_builder(match)

        result = model.predict(features)[0]

        if result == 1:
            outcome = "Home Win"
        elif result == 0:
            outcome = "Draw"
        else:
            outcome = "Away Win"

        predictions.append({
            "home": home,
            "away": away,
            "prediction": outcome
        })

    return predictions