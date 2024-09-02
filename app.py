import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score
import xgboost as xgb
import joblib

# Function to train the model
def train_model(data):
    # Assuming the last column is the target
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    # Encode the target variable
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)
    
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Standardize the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    # Create and train an XGBoost classifier
    model = xgb.XGBClassifier(eval_metric='mlogloss')
    model.fit(X_train, y_train)
    
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    
    return model, accuracy

# Streamlit app
st.title("XGBoost Model Trainer")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.write(data.head())
    
    model, accuracy = train_model(data)
    
    st.write(f"Model Accuracy: {accuracy:.2f}")
    
    # Save the model to a file
    model_filename = "xgboost_model.pkl"
    joblib.dump(model, model_filename)
    
    # Provide a download link for the model
    with open(model_filename, "rb") as file:
        btn = st.download_button(
            label="Download model",
            data=file,
            file_name=model_filename,
            mime="application/octet-stream"
        )
