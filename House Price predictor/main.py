import pickle

from flask import Flask, render_template, request
import pandas as pd
import numpy as np


app = Flask(__name__, template_folder='template')
data = pd.read_csv('C://Users//sherp//Desktop//Python_Project//major_project//Cleaned_data.csv')
pipe = pickle.load(open("C://Users//sherp//Desktop//Python_Project//major_project//RidgeModel.pkl",'rb'))


@app.route("/")
def Hello():

    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)


@app.route('/predict', methods=['POST'])
def predict():

    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bath = request.form.get('bath')
    sqft = request.form.get('total_sqft')



    print(location, bhk, bath, sqft)
    input = pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])
    prediction = pipe.predict(input)[0]
    pd.DataFrame([])
    print(input)
    return str(prediction*10000*80)

if __name__=="__main__":
    app.run(debug=True)