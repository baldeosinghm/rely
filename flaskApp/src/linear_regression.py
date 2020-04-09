import pandas as pd
import numpy as np
import matplotlib
import time
from datetime import datetime
matplotlib.use("TKagg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def predictPrice(stock, days):
    # make data frame
    df = pd.read_csv("csv/" + stock + ".csv", sep='\s*,\s*', header=0, encoding='ascii', engine='python')
    # Store the "Low" in the x var, and the "High" in the y var.  We want to use the Low as the predictor, the independent variable
    X = df['Low'].values.reshape(-1,1)
    y = df['High'].values.reshape(-1,1)
    # Here we split the data: 80% for training, 20% for testing in test_size
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    # Here we train our algorithm, the var "regressor"
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    df['Prediction'] = df['High'].shift(days)
    # Set X_forecast equal to the last 30 rows of the original data set from Close column
    y_forecast = df.drop(['Date', 'Open', 'Close', 'Low', 'Prediction'],1)[days:]
    prediction = regressor.predict(y_forecast)
    return prediction[0]
