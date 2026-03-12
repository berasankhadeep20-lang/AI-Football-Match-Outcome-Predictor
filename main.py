import os
import pandas as pd

from src.api_fetcher import fetch_matches
from src.data_collector import build_dataset
from src.team_stats import compute_team_stats
from src.ml_model import train_model
from src.predictor import predict_match
from src.visualization import plot_goal_distribution, plot_odds_distribution


print("Downloading matches...")

api_data = fetch_matches()

df = build_dataset(api_data)

if df.empty:
    print("Dataset empty. Check API response.")
    exit()

os.makedirs("data", exist_ok=True)

df.to_csv("data/matches.csv", index=False)

print("Dataset saved")

print("Computing team statistics...")

stats = compute_team_stats(df)

print("Training ML model...")

model = train_model(df)

print("Creating visualizations...")

plot_goal_distribution(df)
plot_odds_distribution(df)

print("\nExample prediction")

home_odds = float(input("Home win odds: "))
draw_odds = float(input("Draw odds: "))
away_odds = float(input("Away win odds: "))

prediction = predict_match(home_odds, draw_odds, away_odds, model)

print("Predicted outcome:", prediction)
from src.todays_matches import fetch_today_matches
from src.feature_builder import build_features
from src.match_predictor import predict_today_matches

print("\nFetching today's matches...")

today_matches = fetch_today_matches()

if not today_matches:
    print("No matches today.")
    exit()

predictions = predict_today_matches(
    today_matches,
    model,
    build_features
)

print("\nToday's Predictions\n")

for p in predictions:

    print(
        p["home"],
        "vs",
        p["away"],
        "→",
        p["prediction"]
    )