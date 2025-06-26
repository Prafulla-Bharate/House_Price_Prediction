# 🏠 House Price Prediction Web App

This is a **Streamlit-based web application** that predicts house prices based on various input features such as number of bedrooms, square footage, location, and more. The model was trained using historical housing data and saved using `pickle`.

---

## 🚀 Features

- Clean and interactive UI using Streamlit
- Predict house prices using a pre-trained regression model
- Real-time input for various home attributes
- Encodes categorical and numerical features to match the model's requirements

---

## 🧠 Model Details

- Machine learning model trained on housing dataset (e.g., from Kaggle or similar)
- Could use algorithms like Linear Regression, XGBoost, or Random Forest
- Trained in `HousePrediction.ipynb`
- Saved as `house_price_model.pkl`

---

## 📂 Project Structure

├── app.py # Streamlit app for live prediction
├── HousePrediction.ipynb # Jupyter notebook for model training
├── house_price_model.pkl # Trained and pickled ML model
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🛠️ Tech Stack

- Python 3.8+
- Streamlit
- Pandas, NumPy
- Scikit-learn or XGBoost (based on your model)

---

## 💻 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/house-price-predictor.git
cd house-price-predictor
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Web App
bash
Copy
Edit
streamlit run app.py
🔍 Input Features
bedrooms, bathrooms, sqft_living, sqft_lot

floors, waterfront, view, condition, grade

sqft_above, sqft_basement, yr_built, yr_renovated

zipcode, lat, long

sqft_living15, sqft_lot15

date (if encoded)

🎯 Output
Displays the estimated house price in USD:

💰 Estimated House Price: $XXX,XXX.XX
