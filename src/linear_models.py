# setup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# make data frame
df = pd.read_csv("../csv/apple.csv", sep='\s*,\s*', header=0, encoding='ascii', engine='python')

def show_simple_plot():
    # plot the dataset
    df.plot(x='Low', y='High', style='o')
    # Give graph a name
    plt.title("Apple's High vs Apple's Low")
    plt.xlabel("low")
    plt.ylabel('high')
    plt.show()  ## --> Show the graph


def train_algorithm():
    # Store the "Low" in the x var, and the "High" in the y var
    # We want to use the Low as the predictor, the independent variable
    # Snapchat's High is the dependent variable, what we want to predict
    X = df['Low'].values.reshape(-1,1)
    y = df['High'].values.reshape(-1,1)

    # Split data percentage; 80% for training, 20% for testing
    # We'll use sklearn's Linear Model to allocate that 20% in the var, test_size
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # We need to import LinearRegression class, instantiate it,
    # and call the fit() method along with our training data.

    # We are officially beginning to train the algorithm
    # Create Linear Regression object
    regressor = LinearRegression()
    regressor.fit(X_train, y_train) #training the algorithm

    #To retrieve the intercept:
    print("Regression Line's intercept:")
    print(regressor.intercept_)
    #For retrieving the slope:
    print("Regression Line's slope:")
    print(regressor.coef_)
    print("______________________________________\n")

    # We find that for every 1% increase in Snapchat's Low, the High also increase's by 1%
    # Actual number is 1.046237


def algorithm_predictions():
    # Make predictions of Snap's High using the algorithm
    y_pred = regressor.predict(X_test)
    test_df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
    print("Loading Actual Prices vs. Predicted... \n")
    print(test_df) ## --> Show data frame comparison of actual vs. predicted
    print("______________________________________\n")

    # Plot algorithm line w/ the test data
    plt.scatter(X_test, y_test,  color='gray')
    plt.plot(X_test, y_pred, color='red', linewidth=2)
    plt.show()   ## --> Show the graph (this will indicate if our algorithm, not necessarily if it's accurate)


def algorithm_accuracy():
    # Evaluate the performance of the regression algorithm by using the following three metrics
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
