# TEJESWARA SAI REDDY KARRI (TP062689) APD3F2302CS(DA)
print(" TEJESWARA SAI REDDY KARRI (TP062689)")
print(" FYP - SRI LANKA HOUSE PRICE PREDICTION FLASK SERVER")
from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
    'locations':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_house_price', methods=['POST'])
def price_predict():
    # baths, land_size, beds, house_size, location
    baths = int(request.form['baths'])
    land_size = float(request.form['land_size'])
    beds = int(request.form['beds'])
    house_size = float(request.form['house_size'])
    location = request.form['location']

    response = jsonify({
        'price_predict':util.price_predict(baths, land_size, beds, house_size, location)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python flask server for FYP-House Price Prediction")
    app.run(host="0.0.0.0", port=5000)