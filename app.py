from flask import Flask, render_template, request, jsonify
from predictor import predict_loan

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    if request.is_json:
        data = request.get_json()

        data["education"] = 1 if data["education"] == "Graduate" else 0
        data["self_employed"] = 1 if data["self_employed"] == "Yes" else 0

        prediction, confidence = predict_loan(data)

        return jsonify({
            "prediction": prediction,
            "confidence": confidence
        })

    # HTML Form
    data = {
        "no_of_dependents": int(request.form["no_of_dependents"]),
        "education": int(request.form["education"]),
        "self_employed": int(request.form["self_employed"]),
        "income_annum": float(request.form["income_annum"]),
        "loan_amount": float(request.form["loan_amount"]),
        "loan_term": int(request.form["loan_term"]),
        "cibil_score": int(request.form["cibil_score"]),
        "residential_assets_value": float(request.form["residential_assets_value"]),
        "commercial_assets_value": float(request.form["commercial_assets_value"]),
        "luxury_assets_value": float(request.form["luxury_assets_value"]),
        "bank_asset_value": float(request.form["bank_asset_value"]),
    }

    prediction, confidence = predict_loan(data)

    return render_template(
        "result.html",
        prediction=prediction,
        confidence=confidence
    )


if __name__ == "__main__":
    app.run(debug=True)