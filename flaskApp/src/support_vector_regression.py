import matplotlib
import time
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
matplotlib.use("TKagg")

def vector_predictPrice(stock, days):
    # make data frame
    df = pd.read_csv("csv/" + stock + ".csv", sep='\s*,\s*', header=0, encoding='ascii', engine='python')
    # Store the "Low" in the x var, and the "High" in the y var
    # We want to use the Low as the predictor, the independent variable
    # Stock's High is the dependent variable, what we want to predict
    low = df['Low'].values.reshape(-1,1)
    high = df['High'].values.reshape(-1,1)
    df['Prediction'] = df['High'].shift(days)
    X = df.drop(['Date', 'Open', 'High', 'Low'],1)[days:]
    X = X[:-forecast_out]
    y = np.array(df['Prediction'])
    y = y[:-forecast_out]
    # Here we split the data: 70% for training, 30% for testing in test_size
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    # Instantiate Support Vector Machine (SVR) from SVR class
    # Because we are dealing with a nonlinear relationship, we will specify
    # the kernel function as rbf, for exponential.  The associated keyword
    # is gamma, which must be greater than 0.
    svm_regressor = SVR(kernel='rbf', C=1e3, gamma=0.1)
    # Train SVR algorithm by fitting model
    svm_regressor.fit(x_train, y_train)
    # Drop unessential columns
    y_forecast = df.drop(['Date', 'Open', 'High', 'Low'],1)[days:]
    prediction = svm_regressor.predict(y_forecast)
    return prediction[days]
