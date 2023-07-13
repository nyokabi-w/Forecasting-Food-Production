import streamlit as st
import requests
from PIL import Image
import pandas as pd
import pickle

# Load the pickled forecast DataFrame
with open('forecast.pkl', 'rb') as f:
    forecast_df = pickle.load(f)

# Streamlit app code
st.title("Forecast for Specific Year")

# Add the flag of Kenya from the provided image URL
response = requests.get("https://github.com/Muramati/FAOStat-Dataset-Time-Series/assets/70520367/30563c28-b0dd-4a1f-ad03-4e45385f8d1b")
# image = Image.open(BytesIO(response.content))
# st.image(image, caption="Flag of Kenya", use_column_width=True)

# Prompt the user to enter a specific year
target_year_input = st.text_input("Enter the target year for prediction:")

# Display the forecast for the target year
if target_year_input in forecast_df.index.year.astype(str):
    target_forecast = forecast_df.loc[forecast_df.index.year == int(target_year_input)]
    st.subheader(f"Forecast for {target_year_input}:")
    st.dataframe(target_forecast)
else:
    st.write(f"No forecast available for {target_year_input}.")
