from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import streamlit as st


st.title("Tesla Stock Prediction")

MODEL_PATH = Path("Future Stock price prediction.pkl")
SCALER_PATH = Path("scaler.pkl")


@st.cache_resource(show_spinner="Loading prediction model...")
def load_assets():
    missing = [str(path) for path in (MODEL_PATH, SCALER_PATH) if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Missing required file(s): {', '.join(missing)}")

    return joblib.load(MODEL_PATH), joblib.load(SCALER_PATH)


try:
    model, scaler = load_assets()
except Exception as e:
    st.error(f"Model or scaler could not be loaded: {e}")
    st.stop()

uploaded_file = st.file_uploader("upload TSLA CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.tail())

    if "Close" not in df.columns:
        st.error("Uploaded CSV must contain a 'Close' column.")
        st.stop()

    close_data = df[["Close"]]
    if len(close_data) < 60:
        st.error("Uploaded CSV must contain at least 60 rows for prediction.")
        st.stop()

    scaled_data = scaler.transform(close_data)
    X = np.array(scaled_data[-60:]).reshape(1, 60, 1)

    prediction = model.predict(X)
    pred_value = float(np.ravel(prediction)[0])
    st.success(f"Predicted Price: {pred_value:.2f}")
