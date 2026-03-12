import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def train_model(df):

    # create target variable
    df["result"] = df.apply(
        lambda x: 1 if x.home_goals > x.away_goals
        else (0 if x.home_goals == x.away_goals else -1),
        axis=1
    )

    X = df[["odds_home", "odds_draw", "odds_away"]]
    y = df["result"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2
    )

    model = RandomForestClassifier(n_estimators=200)

    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    print("Model Accuracy:", accuracy)

    return model