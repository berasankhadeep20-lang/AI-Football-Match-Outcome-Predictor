import pandas as pd

def predict_match(home_odds, draw_odds, away_odds, model):

    features = pd.DataFrame({
        "odds_home": [home_odds],
        "odds_draw": [draw_odds],
        "odds_away": [away_odds]
    })

    prediction = model.predict(features)[0]

    if prediction == 1:
        return "Home Win"
    elif prediction == 0:
        return "Draw"
    else:
        return "Away Win"