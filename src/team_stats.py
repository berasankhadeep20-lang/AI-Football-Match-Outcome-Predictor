import pandas as pd

def compute_team_stats(df):

    stats = {}

    teams = set(df["home_team"]).union(set(df["away_team"]))

    for team in teams:

        home_games = df[df["home_team"] == team]
        away_games = df[df["away_team"] == team]

        goals_scored = home_games["home_goals"].sum() + away_games["away_goals"].sum()
        goals_conceded = home_games["away_goals"].sum() + away_games["home_goals"].sum()

        matches = len(home_games) + len(away_games)

        if matches == 0:
            continue

        stats[team] = {
            "avg_scored": goals_scored / matches,
            "avg_conceded": goals_conceded / matches,
            "matches": matches
        }

    return stats