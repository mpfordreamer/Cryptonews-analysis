import pickle
from flask import Flask, request, jsonify

# Load model
with open("Membangun_model/best_lgbm_model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text")

    # Dummy preprocessing
    processed_text = text.lower()  # Contoh sederhana
    tfidf = TfidfVectorizer(max_features=2000)
    X = tfidf.fit_transform([processed_text]).toarray()

    prediction = model.predict(X)[0]
    
    return jsonify({
        "sentiment": "Positive" if prediction == 2 else "Neutral" if prediction == 1 else "Negative",
        "raw_input": text,
        "prediction_code": int(prediction)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)