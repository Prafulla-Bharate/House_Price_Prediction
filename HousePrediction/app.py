import streamlit as st
import pickle
import pandas as pd

st.title("🏠 House Price Prediction App")

# Load trained model
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

# Collect user input
st.header("Enter Property Details")

bedrooms = st.number_input("Bedrooms", min_value=0, value=3)
bathrooms = st.number_input("Bathrooms", min_value=0.0, value=2.0)
sqft_living = st.number_input("Living Area (sqft)", min_value=0, value=1800)
sqft_lot = st.number_input("Lot Area (sqft)", min_value=0, value=5000)
floors = st.number_input("Floors", min_value=0.0, value=1.0)
waterfront = st.selectbox("Waterfront View", ["No", "Yes"])
view = st.slider("View Rating (0-4)", 0, 4, 0)
condition = st.slider("Condition (1-5)", 1, 5, 3)
grade = st.slider("Grade (1-13)", 1, 13, 7)
sqft_above = st.number_input("Above Ground sqft", min_value=0, value=1500)
sqft_basement = st.number_input("Basement sqft", min_value=0, value=300)
yr_built = st.number_input("Year Built", min_value=1900, max_value=2025, value=2000)
yr_renovated = st.number_input("Year Renovated (0 if never)", min_value=0, max_value=2025, value=0)
zipcode = st.number_input("Zipcode", value=98103)
lat = st.number_input("Latitude", value=47.65)
long = st.number_input("Longitude", value=-122.35)
sqft_living15 = st.number_input("Living Area (Nearby homes)", min_value=0, value=1800)
sqft_lot15 = st.number_input("Lot Area (Nearby homes)", min_value=0, value=5000)
date = st.number_input("Encoded Date", value=100)  # if label encoded in training

# Create DataFrame
input_data = pd.DataFrame([{
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "sqft_living": sqft_living,
    "sqft_lot": sqft_lot,
    "floors": floors,
    "waterfront": 1 if waterfront == "Yes" else 0,
    "view": view,
    "condition": condition,
    "grade": grade,
    "sqft_above": sqft_above,
    "sqft_basement": sqft_basement,
    "yr_built": yr_built,
    "yr_renovated": yr_renovated,
    "zipcode": zipcode,
    "lat": lat,
    "long": long,
    "sqft_living15": sqft_living15,
    "sqft_lot15": sqft_lot15,
    "date": date
}])

# Ensure column match
if hasattr(model, 'feature_names_in_'):
    required_cols = model.feature_names_in_
    missing_cols = set(required_cols) - set(input_data.columns)
    for col in missing_cols:
        input_data[col] = 0
    input_data = input_data[required_cols]

# Predict
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated House Price: ${prediction[0]:,.2f}")
