# app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import tensorflow as tf
from tensorflow import keras

st.set_page_config(page_title="Supply Chain Demand Forecasting Dashboard", layout="wide")

# ---------- Title ----------
st.title("Supply Chain Demand Forecasting Dashboard")

# ---------- Load Dataset ----------
st.header("1. Load Dataset")
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Dataset Preview:")
    st.dataframe(data.head())

    # ---------- Data Cleaning ----------
    st.header("2. Data Cleaning & Feature Engineering")
    data = data.dropna()
    if 'Date' in data.columns:
        data['Date'] = pd.to_datetime(data['Date'])
        data['Month'] = data['Date'].dt.month
        data['DayOfWeek'] = data['Date'].dt.dayofweek
        data['Quarter'] = data['Date'].dt.quarter
        data = data.drop(columns=['Date'])
    categorical_cols = ['Promotion', 'Weather', 'EconomicIndicators']
    for col in categorical_cols:
        if col in data.columns:
            data = pd.get_dummies(data, columns=[col])
    
    st.write("Cleaned Dataset Preview:")
    st.dataframe(data.head())

    # ---------- Feature & Target ----------
    target = 'HistoricalSales'
    if target not in data.columns:
        st.error(f"Target column '{target}' not found in dataset!")
    else:
        features = data.drop(columns=[target])
        X_train, X_test, y_train, y_test = train_test_split(
            features, data[target], test_size=0.2, random_state=42
        )
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # ---------- Model Training ----------
        st.header("3. Train Neural Network Model")
        train_model = st.checkbox("Train Model", value=False)
        if train_model:
            model = keras.Sequential([
                keras.layers.Dense(128, activation='relu', input_shape=[X_train_scaled.shape[1]]),
                keras.layers.Dense(64, activation='relu'),
                keras.layers.Dense(32, activation='relu'),
                keras.layers.Dense(1)
            ])
            model.compile(optimizer='adam', loss='mse')
            history = model.fit(
                X_train_scaled, y_train, epochs=50, validation_split=0.2, verbose=0
            )
            st.success("Model Trained Successfully!")

            # Plot training history
            st.subheader("Training History")
            plt.plot(history.history['loss'], label='train')
            plt.plot(history.history['val_loss'], label='val')
            plt.xlabel('Epoch')
            plt.ylabel('Mean Squared Error')
            plt.legend()
            st.pyplot(plt)

            # Save model
            model.save("demand_forecasting_model.h5")
        else:
            model = keras.models.load_model("demand_forecasting_model.h5")
            st.info("Loaded pre-trained model.")

        # ---------- Model Evaluation ----------
        st.header("4. Model Evaluation")
        test_predictions = model.predict(X_test_scaled)
        mse = mean_squared_error(y_test, test_predictions)
        st.write(f"Mean Squared Error on Test Set: {mse:.2f}")

        # Plot True vs Predicted
        st.subheader("True vs Predicted Sales")
        plt.figure(figsize=(6, 4))
        plt.scatter(y_test, test_predictions)
        plt.xlabel('True Sales')
        plt.ylabel('Predicted Sales')
        plt.title('True vs Predicted Sales')
        st.pyplot(plt)

        # ---------- Interactive Prediction ----------
        st.header("5. Predict Future Sales")
        st.write("Enter values for prediction:")

        user_input = {}
        for feature in features.columns:
            val = st.number_input(f"{feature}", value=float(features[feature].mean()))
            user_input[feature] = val

        if st.button("Predict Sales"):
            input_df = pd.DataFrame([user_input])
            input_scaled = scaler.transform(input_df)
            prediction = model.predict(input_scaled)
            st.success(f"Predicted Sales: {prediction[0][0]:.2f}")
