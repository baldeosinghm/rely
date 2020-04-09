import pandas as pd
import numpy as np
import matplotlib
import time
from datetime import datetime
matplotlib.use("TKagg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.linear_model import LinearRegression

def predictPrice(stock, days):
    # make data frame
    df = pd.read_csv("csv/" + stock + ".csv", sep='\s*,\s*', header=0, encoding='ascii', engine='python')
    # Store the "Low" in the x var, and the "High" in the y var
    # We want to use the Low as the predictor, the independent variable
    # Stock's High is the dependent variable, what we want to predict
    X = df['Low'].values.reshape(-1,1)
    y = df['High'].values.reshape(-1,1)
    # Here we split the data: 70% for training, 30% for testing in test_size
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    # Here we train our algorithm, "regressor"
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    # Forecast out 30 days
    # Shift data frame columns down 30
    df['Prediction'] = df['High'].shift(days)
    # Set X_forecast equal to the last 30 rows of the original data set from Close column
    y_forecast = df.drop(['Date', 'Open', 'High', 'Low'],1)[days:]
    prediction = regressor.predict(y_forecast)
    regressor_confidence = regressor.score(X_test, y_test)
    kFold_prediction = cross_val_predict(regressor, X, y, cv=3)
    kFold_score = cross_val_score(regressor, X, y, cv=3)
    return prediction[days]
