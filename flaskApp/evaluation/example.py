import pandas as pd
import numpy as np
# import matplotlib
# matplotlib.use("TKagg")
# import matplotlib.pyplot as plt
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
    # Here we split the data: 80% for training, 20% for testing in test_size
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    # Here we train our algorithm, "regressor"
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    # Forecast out inputted # of days
    # Shift data frame columns up to predict "days" amount into the future
    df['Prediction'] = df['High'].shift(days)
    # Drop unessential columns and remove "days" amount of bottom rows
    y_forecast = df.drop(['Date', 'Open', 'High', 'Low'],1)[days:]
    prediction = regressor.predict(y_forecast)

    # Evaluate the performance of the Linear Regression algorithm by using the following four metrics
    print('R^2:', metrics.score(y_test, y_pred))
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    print("______________________________________\n")

    return prediction[days]
