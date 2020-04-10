import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("TKagg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.linear_model import LinearRegression

def cvPredictPrice(stock, days):
    # make data frame
    df = pd.read_csv("csv/" + stock + ".csv", sep='\s*,\s*', header=0, encoding='ascii', engine='python')
    # Store the "Low" in the x var, and the "High" in the y var
    # We want to use the Low as the predictor, the independent variable
    # Stock's High is the dependent variable, what we want to predict
    X = df['Low'].values.reshape(-1,1)
    y = df['High'].values.reshape(-1,1)
    # Here we split the data: 80% for training, 20% for testing in test_size
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    # Here we train our algorithm, "regressor"
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    # Use sklearns "cross_val_predict" method to take the estimator and
    # perform a lerning algorithm over three subsets of the original
    # dataset; cv is the # of partitioned subsets
    # The prediction functions trains on the X (predictors) and y (outcome)
    kFold_prediction = cross_val_predict(regressor, X, y, cv=5)
    # Return forecast from inputted # of days
    return kFold_prediction[days]
