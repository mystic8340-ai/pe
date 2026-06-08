# Streamlit Deployment

Use these settings on Streamlit Community Cloud:

1. Repository: this GitHub repo.
2. Branch: the branch where these files are pushed.
3. Main file path: `app.py`.
4. Advanced settings: select Python `3.11`.

Important files that must be present in the GitHub repo:

- `app.py`
- `requirements.txt`
- `Future Stock price prediction.pkl`
- `scaler.pkl`

`runtime.txt` is useful for some hosts, but Streamlit Community Cloud sets Python from the deployment Advanced settings instead.
