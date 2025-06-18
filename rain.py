import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. LOAD DATA DIRECTLY (no file uploader)
def load_data():

    df = pd.read_csv("Rainfall.csv") 

    if 'day' in df.columns:
        df.drop(columns=['day'], inplace=True)

    df['rainfall'] = df['rainfall'].map({'yes': 1, 'no': 0})

    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    return df

def preprocess_data(df: pd.DataFrame):
    X = df.drop(columns=['rainfall'])
    y = df['rainfall']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )
    return X_train, X_test, y_train, y_test, scaler

def train_model(X_train, y_train):

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def main():
    st.title("Rainfall Prediction App ☔")
    st.write("Predict whether it will rain based on weather parameters.")

    df = load_data()
    X_train, X_test, y_train, y_test, scaler = preprocess_data(df)
    
    model = train_model(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    st.subheader("Model Performance on Test Data")
    st.write(f"**Accuracy**: {accuracy:.2f}")
    
    if st.checkbox("Show Classification Report"):
        report = classification_report(y_test, y_pred, target_names=["No Rain", "Rain"])
        st.text(report)
    
    st.subheader("Try a Custom Prediction")
    st.write("Enter weather parameters below to see if it will rain.")

    feature_cols = [col for col in df.columns if col != 'rainfall']

    user_input = {}
    for col in feature_cols:
        default_val = float(df[col].mean())
        user_input[col] = st.number_input(f"{col}", value=default_val)

    if st.button("Predict"):
        input_df = pd.DataFrame([user_input])
        
        input_scaled = scaler.transform(input_df)
        
        prediction = model.predict(input_scaled)[0]
        
        if prediction == 1:
            st.success("**It will RAIN.** ☔")
        else:
            st.info("**No rain expected.** ☀️")

if __name__ == "__main__":
    main()
