# main.py

import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# 1. Initialize the FastAPI app
app = FastAPI(title="California Housing Price Predictor", version="1.0")

# 2. Load the trained model
# Make sure 'linear_regression_model.pkl' is in the same directory
try:
    with open('linear_reg_model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    print("Model file not found. Please ensure 'linear_reg_model.pkl' is present.")
    model = None # Set model to None if file is not found

# 3. Define the input data model using Pydantic
# This ensures that the input data has the correct structure and data types.
class HouseFeatures(BaseModel):
    latitude: float
    longitude: float
    population: int
    households: int
    total_rooms: int
    
    # Example to show what the input should look like in the docs
    class Config:
        schema_extra = {
            "example": {
                "latitude": 37.88,
                "longitude": -122.23,
                "population": 322,
                "households": 126,
                "total_rooms": 880
            }
        }

# 4. Create the API endpoints

# Root endpoint for a simple health check
@app.get("/")
def read_root():
    """A simple endpoint to check if the API is running."""
    return {"status": "ok", "message": "Housing Price Prediction API is running!"}

# Prediction endpoint
@app.post("/predict/")
def predict_bedrooms(features: HouseFeatures):
    """
    Predicts the number of total bedrooms based on input features.
    """
    if model is None:
        return {"error": "Model is not loaded. Cannot make predictions."}
        
    # Convert the input data into a pandas DataFrame
    # The model expects a DataFrame with specific column names
    input_df = pd.DataFrame([features.dict()])
    
    # Reorder columns to match the model's training order
    # This is crucial for the model to work correctly
    feature_order = ['latitude', 'longitude', 'population', 'households', 'total_rooms']
    input_df = input_df[feature_order]

    # Make a prediction
    prediction = model.predict(input_df)
    
    # Return the prediction
    return {"predicted_total_bedrooms": round(prediction[0], 2)}