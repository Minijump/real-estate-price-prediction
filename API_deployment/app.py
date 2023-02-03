from predict.prediction import predict as pred
from Preprocessing.cleaning_data import preprocess

#from flask import Flask, jsonify, request
from flask import Flask, jsonify, request, render_template

#Invoke-WebRequest -Method POST -Uri "http://127.0.0.1:5000/predict" -Body '{"data":{"Living_Area": 90, "Type_of_property": "HOUSE", "Number_of_rooms": 4, "Locality": 6637, "Swimming_pool": 0}}' -ContentType "application/json" -Headers @{'Content-Type'='application/json'}
#the request above in anaconda POWERSHELL prompt
# # or localhost:5000 in the browser

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_get():
    return jsonify({"message": "alive"})

@app.route('/predict', methods=['GET'])
def handle_get_predict():
    return jsonify({"message": "Please send a POST request to this endpoint with the following JSON format data in the request body: {\"Living_Area\": int, \"Type_of_property\": \HOUSE\/ APARTMENT, \"Number_of_rooms\": int, \"Locality\": int, \"Swimming_pool\": bool}"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    preprocessed_data = preprocess(data['data'])
    price = pred(preprocessed_data)
    return jsonify({"prediction": price, "status code": 200})
    

if __name__ == '__main__':
    app.run(port=5000, debug=True)