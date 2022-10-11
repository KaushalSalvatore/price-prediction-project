from flask import Flask, Blueprint,render_template,jsonify , request
from flask_cors import cross_origin
from PricePrediction.laptop.artifacts.modal.backEnd import backEnd


laptop_blueprint = Blueprint('laptop', __name__)


@laptop_blueprint.route("/laptopprice")
@cross_origin()
def laptop():
    return render_template("laptop_index.html")



@laptop_blueprint.route('/laptoppricepredict', methods=['POST'])
def home():
    screenSize = float( request.form['screenSize'])
    screenRes = int(request.form['ScreenRes'])
    Cpu = int(request.form['CPU'])
    RAM = int(request.form['RAM'])
    weight = float(request.form['Weight'])
    touchScreen = int(request.form['Touchscreen'])
    HDD = int(request.form['HDD'])
    SSD = int(request.form['SSD'])
    SSHD = int(request.form['SSHD'])
    FStorage = int(request.form['fStorage'])
    Type = int(request.form['Type'])
    Os = int(request.form['Os'])
    back = backEnd(screenSize, screenRes, Cpu, RAM, weight, touchScreen, HDD, SSD, SSHD, FStorage, Type, Os)
    final_predicted = (round(float(back.totalPredicted[0]),2))
    
    return render_template('predicted_price.html', prediction_text = 'Predicted Laptop Price is €{} (EUR)'.format(final_predicted))
