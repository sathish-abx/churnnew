from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

# Load the encoders and model
with open("backend//encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

with open("backend//customer_churn_model.pkl", "rb") as f:
    model_data = pickle.load(f)
    model = model_data["model"]
    feature_names = model_data["features_names"]

# Define input data model using Pydantic
class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow requests from React app
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Define prediction endpoint
@app.post("/predict")
def predict_churn(data: CustomerData):
    try:
        # Convert input data to DataFrame
        input_data = data.dict()
        input_df = pd.DataFrame([input_data])

        # Encode categorical features using the loaded encoders
        for column, encoder in encoders.items():
            input_df[column] = encoder.transform(input_df[column])

        # Ensure the columns are in the correct order
        input_df = input_df[feature_names]

        # Make prediction
        prediction = model.predict(input_df)
        pred_prob = model.predict_proba(input_df)

        # Prepare response
        result = "Churn" if prediction[0] == 1 else "No Churn"
        churn_probability = pred_prob[0][1] * 100  # Probability of Churn in percentage

        return {
            "result": result,
            "churn_probability": round(churn_probability, 2)
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)