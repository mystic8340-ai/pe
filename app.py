import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("Tesla Stock Prediction")
try:
    model = joblib.load("Future Stock price prediction.pkl")
    scaler = joblib.load("scaler.pkl")
except Exception as e:
    st.error(f"Model or scaler could not be loaded: {e}")
    model = None
    scaler = None
uploaded_file=st.file_uploader(
    "upload TSLA CSV",
    type=["csv"]
)
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df.tail())
    close_data=df[['Close']]
    if scaler is None:
        st.error("Scaler not available — model dependencies may be missing on this system.")
    else:
        scaled_data=scaler.transform(close_data)
        last_60=scaled_data[-60:]
        X=np.array(last_60)
        X=X.reshape(1,60,1)
        if model is None:
            st.error("Model not available — cannot make predictions.")
        else:
            prediction = model.predict(X)
            try:
                pred_value = float(prediction.ravel()[0])
            except Exception:
                pred_value = prediction[0]
            st.success(f"Predicted Price: {pred_value:.2f}")
    