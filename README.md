## Price Estimating Web Project
This is machine learning web application to predict the selling price of
House Price , Flight Price , Insurance Price, Laptop Price, Mobile Price,
Used car Price. Highly comprehensive analysis with all data cleaning, exploration, 
visualization, feature selection, model building, evaluation, and assumptions with 
validity steps.

## Problem Statements

#### Flight 
Created a web application  that estimates Flight Prices to help users look for best prices when booking flight tickets.
Engineered features from the Departure Time, Date of Journey, to quantify the data and make it more understandable. Optimized multiple Regression models

#### Bengaluru House 
Buying a home, especially in a city like Bengaluru, is a tricky choice. While the major factors are usually the 
same for all metros, there are others to be considered for the Silicon Valley of India. With its help millennial crowd, 
vibrant culture, great climate and a slew of job opportunities, it is difficult to ascertain the price of a house in Bengaluru.

#### Laptop
The dataset is about laptops configuration with prices containing 1303 laptop data with 12 columns Company name,type namee, 
laptop size in (inches), Screen resolution, CPU, RAM, Memory, GP, Operating system, Price in INR. this is Machine Leaning Problem and It is a Regresion problem, 
for a given columns we need to predict the price of laptop.

#### Insurance
People are always confused about their medical insurance and don't know the cost of insurance at different ages and conditions. 
This web application is useful for these people and is useful to make predictions of the insurance cost they will have to pay.

#### Mobile
In this project, we are going to explore and analyze a dataset which contains specifications of two thousand mobile phones and try to 
predict optimum price ranges for a list of mobile phones in the market by applying various machine learning algorithms

#### Used Car
it is not easy to solve as the car's value depends on many factor including year of registration, manufacturer, model, mileage, 
horsepower, origin and several other specific informations such as type of fuel and braking sysrem, condition of bodywork and interiors, 
interior materials (plastics of leather), safery index, type of change (manual, assisted, automatic, semi-automatic), number of doors, 
number of previous owners, if it was previously owned by a private individual or by a company and the prestige of the manufacturer.

## If you want to view the deployed project, click on the following link:

https://estimated-price.herokuapp.com/

## Screenshots
![Alt text](/PricePrediction/static/assets/images/screenshots/01.png?raw=true "Screen 1")
![Alt text](/PricePrediction/static/assets/images/screenshots/02.png?raw=true "Screen 2")
![Alt text](/PricePrediction/static/assets/images/screenshots/03.png?raw=true "Screen 3")
![Alt text](/PricePrediction/static/assets/images/screenshots/04.png?raw=true "Screen 4")

## Project Demo
![Alt text](/PricePrediction/static/assets/images/screenshots/demo.gif?raw=true "Screen demo")

## dataSet links 
1. [Flight Price](https://www.kaggle.com/datasets/nikhilmittal/flight-fare-prediction-mh)      
2. [Bengaluru House Price](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data) 	
3. [Insurance Price](https://www.kaggle.com/datasets/rajgupta2019/medical-insurance-dataset)    
4. [Laptop Price](https://www.kaggle.com/datasets/mohidabdulrehman/laptop-price-dataset)	
5. [Mobile Price](https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification)  
6. [Used car Price](https://www.kaggle.com/datasets/avikasliwal/used-cars-price-prediction)

## Roadmap

- Data Collection
- Data Analysis
- Data Visualization
- Feature Engineering
- Feature Selection
- Model Building
- Model Evalution
- Hyper Parameter Tunning
- Creating Pickle file
- Web App using Flask
- Deployment


## Tech Stack

**python packages:** Pandas, Numpy, Scikit-learn, matplotlib

**ML Algorithms:** LinearRegression,RandomizedSearchCV,RandomForestRegressor,XGBRegressor

**Framework:** Flask

**frontend:** Html, CSS



## Run Locally

Clone the project

```bash
  git clone https://github.com/KaushalSalvatore/price-prediction-project.git
```
Install dependencies

```bash
  pip install -r requirements. txt
```

Start the local server

```bash
  Python server.py or server.py
```


## Deploy on Github

To deploy this project on github use this following command in the project folder.

Initializing a new repository
```bash
  git .init
```

A gitignore file specifies intentionally untracked files that Git should ignore.
```bash
  touch .gitignore
```
Add all the files 
```bash
  git add .
```
Check file status 
```bash
  git status
```
Commit all the file on git
```bash
  git commit -m "your message"
```
Push all the code on github
```bash
  git push <your_branch_name>
```
Push code forcefully 

```bash
  git push origin <your_branch_name> --force
```




## Deploy on heroku

To deploy project on heroku server use this following command.

login in heroku server
```bash
  login heroku
```
Install gunicorn
```bash
  pip install gunicorn
```
Create procfile
```bash
  touch Procfile
```
Create requirements text file 
```bash
  pip freeze > requirements.txt
```
Creates a new empty application on Heroku
```bash
  heroku create -a "project name"
```
Add a remote to your local repository 
```bash
  git remote -v
```
push the code in heroku master branch
```bash
  git push heroku master
```
## Feedback

if you have any suggetion and feedback and need any kind of project related help reach me out at
[linkedin](https://www.linkedin.com/in/kaushal-pandey-067898165/)

#### Thank You 