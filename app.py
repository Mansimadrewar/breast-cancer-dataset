import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("best_model.pkl", "rb"))
# Set page title
st.set_page_config(page_title="Breast Cancer Prediction App", page_icon="🩺")

# App title
st.title("🩺 Breast Cancer Classification")
st.write("Predict whether a tumor is **Benign (0)** or **Malignant (1)** using clinical measurements.")

# Sidebar inputs
st.sidebar.header("Input Features")

def user_input_features():
    radius_mean = st.sidebar.number_input("Radius Mean", 0.0, 30.0, 14.0)
    texture_mean = st.sidebar.number_input("Texture Mean", 0.0, 40.0, 19.0)
    perimeter_mean = st.sidebar.number_input("Perimeter Mean", 0.0, 200.0, 90.0)
    area_mean = st.sidebar.number_input("Area Mean", 0.0, 2500.0, 600.0)
    smoothness_mean = st.sidebar.number_input("Smoothness Mean", 0.0, 0.2, 0.09)
    compactness_mean = st.sidebar.number_input("Compactness Mean", 0.0, 0.4, 0.1)
    concavity_mean = st.sidebar.number_input("Concavity Mean", 0.0, 0.5, 0.05)
    concave_points_mean = st.sidebar.number_input("Concave Points Mean", 0.0, 0.3, 0.03)
    symmetry_mean = st.sidebar.number_input("Symmetry Mean", 0.0, 0.4, 0.18)
    fractal_dimension_mean = st.sidebar.number_input("Fractal Dimension Mean", 0.0, 0.1, 0.06)

    features = np.array([[radius_mean, texture_mean, perimeter_mean, area_mean,
                          smoothness_mean, compactness_mean, concavity_mean,
                          concave_points_mean, symmetry_mean, fractal_dimension_mean]])
    return features

# Collect user input
input_data = user_input_features()

# Predict button
if st.button("🔍 Predict"):
    prediction = model.predict(input_data)
    result = "🟢 Benign (Non-Cancerous)" if prediction[0] == 0 else "🔴 Malignant (Cancerous)"
    st.subheader("Prediction Result:")
    st.success(result)

# Footer
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit and Scikit-learn.")
