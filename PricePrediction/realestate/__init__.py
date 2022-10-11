from flask import Blueprint,render_template,jsonify , request
from flask_cors import cross_origin
from sklearn import utils
import pickle
import json
import numpy as np


realestate = Blueprint("realestate",__name__)

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./PricePrediction/realestate/artifacts/json/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('./PricePrediction/realestate/artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return 

@realestate.route("/")
def index():
    return render_template("index.html")

@realestate.route("/homeprice")
def homeprice():
    load_saved_artifacts()
    print(load_saved_artifacts())
    return render_template("home_index.html")

@realestate.route('/get_location_names', methods=['GET'])
def get_location():
    response = jsonify({
        'locations': get_location_names()
         })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@realestate.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    # response = jsonify({
    #     'estimated_price': get_estimated_price(location,total_sqft,bhk,bath)
    # })
    # response.headers.add('Access-Control-Allow-Origin', '*')
    prediction = get_estimated_price(location,total_sqft,bhk,bath)
    print(prediction)
    # return response
    return render_template('predicted_price.html', prediction_text='Estimate Banglore Home Price is {}.'.format(prediction))



