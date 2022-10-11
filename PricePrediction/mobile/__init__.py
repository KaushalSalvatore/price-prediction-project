import numpy as np
from flask import Blueprint, Flask, render_template, request
import pickle
mobile_blueprint = Blueprint("mobile",__name__)

model = pickle.load(open('PricePrediction/mobile/artifacts/model.pkl','rb'))

@mobile_blueprint.route('/mobileprice')
def home():
    return render_template('mobile_index.html')

@mobile_blueprint.route('/mobilepriceprediction', methods=['POST'])
def predict():
    features = [int(x) for x in request.form.values()]
    print(features)
    final_feat = [np.array(features)]
    print(final_feat)
    print(len(final_feat))
    prediction = model.predict(final_feat)
    if(prediction==0):
        value = '5000 to 10,000'
    elif(prediction==1):
        value = '10,000 to 15,000'
    elif(prediction==2):
        value = '15,000 to 20,000'
    elif(prediction==2):
        value = '20,000 to 30,000'
    return render_template('predicted_price.html', prediction_text = 'Price Score is {}'.format(value))