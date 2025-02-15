from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response

app = Flask(__name__) 
CORS(app)


@app.get("/")
def index_get():
    return render_template("index.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    #TODO: check if text is valid 
    responce = get_response(text)
    message = {"answer":responce }
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)