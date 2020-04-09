import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("TKagg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

def predictNaivePrice(stock, days):
    # make data frame
    df = pd.read_csv("csv/" + stock + ".csv", sep='\s*,\s*', header=0, encoding='ascii', engine='python')
    # Store the "Low" in the x var, and the "High" in the y var
    # We want to use the Low as the predictor, the independent variable
    # Stock's High is the dependent variable, what we want to predict
    X = df['Low'].values.reshape(-1,1)
    y = df['High'].values.reshape(-1,1)
    # Here we split the data: 70% for training, 30% for testing in test_size
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
    # Create instance of sklearn's Gaussian Naive Bayes class
    gnb = GaussianNB()
    # Train Naive-Bayes algorithm by fitting model
    gnb.fit(X_train.astype(int), y_train.astype(int))
    # Forecast out inputted # of days
    # Shift data frame columns up to predict "days" amount into the future
    df['Prediction'] = df['High'].shift(days)
    # Drop unessential columns and remove "days" amount of bottom rows
    y_forecast = df.drop(['Date', 'Open', 'High', 'Low'],1)[days:]
    prediction = gnb.predict(y_forecast)
    # Forecast predictions and return the price
    return prediction[days]
