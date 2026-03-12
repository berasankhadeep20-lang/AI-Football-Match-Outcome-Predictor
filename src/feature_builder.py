import pandas as pd

def build_features(match):

    features = pd.DataFrame({
        "odds_home": [match["odds"]["1"]],
        "odds_draw": [match["odds"]["X"]],
        "odds_away": [match["odds"]["2"]]
    })

    return features