from flask import Flask, render_template
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("fraud_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
