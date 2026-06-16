import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt

# Load model
with open('model_pickle', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="House Price Prediction",
                   page_icon="🏠",
                   layout="wide")

st.title("🏠 House Price Prediction Dashboard")
st.write("Predict house prices based on land area using Linear Regression.")

# Sidebar
st.sidebar.header("Input Parameters")

area = st.sidebar.number_input(
    "Enter Area (Sq.Ft)",
    min_value=100,
    max_value=50000,
    value=1000
)

# Prediction
if st.button("Predict Price"):

    prediction = model.predict([[area]])

    st.success(
        f"Predicted House Price for {area:,} Sq.Ft = ₹ {prediction[0]:,.2f}"
    )

# Optional Dataset Visualization
st.subheader("Area vs Price Relationship")

try:
    df = pd.read_csv("housepriceprediction.csv")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(df["area"], df["price"])
    ax.set_xlabel("Area")
    ax.set_ylabel("Price")
    ax.set_title("Area vs Price")

    st.pyplot(fig)

except:
    st.info("Dataset file not found. Prediction module still works.")
