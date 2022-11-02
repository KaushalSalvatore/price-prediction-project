from flask import Flask , render_template , jsonify , request
from PricePrediction.homePage import homepage
from PricePrediction.insurance import insurance
from PricePrediction.realestate import realestate
from PricePrediction.flight import flight_blueprint
from PricePrediction.laptop import laptop_blueprint
from PricePrediction.mobile import mobile_blueprint
from PricePrediction.usedcar import usedcar_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(homepage)
    app.register_blueprint(insurance)
    app.register_blueprint(realestate) 
    app.register_blueprint(flight_blueprint)
    app.register_blueprint(laptop_blueprint)
    app.register_blueprint(usedcar_blueprint)
    app.register_blueprint(mobile_blueprint)
    return app