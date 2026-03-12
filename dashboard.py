import streamlit as st
import pandas as pd
from src.ml_model import train_model
from src.data_collector import build_dataset
from src.api_fetcher import fetch_matches

st.title("⚽ AI Football Match Predictor")

st.write("Machine Learning football prediction dashboard")

api_data = fetch_matches()
df = build_dataset(api_data)

if df.empty:
    st.error("No dataset available")
    st.stop()

model = train_model(df)

st.subheader("Dataset Preview")

st.dataframe(df.head())

st.subheader("Predict Match Outcome")

home_odds = st.number_input("Home Win Odds", value=2.0)
draw_odds = st.number_input("Draw Odds", value=3.0)
away_odds = st.number_input("Away Win Odds", value=2.5)

if st.button("Predict"):

    import pandas as pd

    features = pd.DataFrame({
        "odds_home":[home_odds],
        "odds_draw":[draw_odds],
        "odds_away":[away_odds]
    })

    prediction = model.predict(features)[0]

    if prediction == 1:
        st.success("Prediction: Home Win")
    elif prediction == 0:
        st.warning("Prediction: Draw")
    else:
        st.error("Prediction: Away Win")