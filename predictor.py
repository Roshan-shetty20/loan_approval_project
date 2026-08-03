import joblib
import numpy as np

# Load the complete pipeline
model = joblib.load("models/loan_approval_pipeline.pkl")


def predict_loan(data):

    features = np.array([[
        data["no_of_dependents"],
        data["education"],
        data["self_employed"],
        data["income_annum"],
        data["loan_amount"],
        data["loan_term"],
        data["cibil_score"],
        data["residential_assets_value"],
        data["commercial_assets_value"],
        data["luxury_assets_value"],
        data["bank_asset_value"]
    ]])

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0]

    confidence = round(max(probability) * 100, 2)

# Remove extra spaces
    prediction = prediction.strip()

    if prediction == "Approved":
        result = "Loan Approved"
    else:
        result = "Loan Rejected"

    return result, confidence