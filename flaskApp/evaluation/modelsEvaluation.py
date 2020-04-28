# To execute any evaluation technique install the below libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


# Visualize plot of stock's high vs low using matplotlib
df.plot(x='Low', y='High', style='o')
# Give graph a name
plt.title("Stock's High vs Stock's Low")
plt.legend()
plt.xlabel("low")
plt.ylabel('high')
plt.show()  ## --> Show the graph


# Determine how far linear model is off from actual values
regressor_confidence = regressor.score(X_test, y_test)
print("Regressor confidence: ", regressor_confidence)


# Test K-Fold Cross Validation accuracy
kFold_prediction = cross_val_predict(regressor, X, y, cv=3)
kFold_score = cross_val_score(regressor, X, y, cv=3)
print(kFold_prediction)
print("______________________________________\n")
print("Accuracy: %0.2f (+/- %0.2f)" % (kFold_score.mean(), kFold_score.std() * 2))


# Test Support Vector Machine's accuracy
svm_confidence = svr_rbf.score(x_test, y_test)
print("svm confidence: ", svm_confidence)


# #To retrieve Linear Regression intercept:
print("Regression Line's intercept:")
print(regressor.intercept_)
print("______________________________________\n")
#For retrieving the slope:
print("Regression Line's slope:")
print(regressor.coef_)


# View collapased data frame to quickly view actual prices vs predictions from Linear Regression algorithm
y_pred = regressor.predict(X_test)
test_df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
print("Loading Actual Prices vs. Predicted... \n")
print(test_df) ## --> Show data frame comparison of actual vs. predicted


# Visualize algorithm's prediction with matplotlib line
plt.scatter(X_test, y_test,  color='gray')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.show()   ## --> Show the graph (this will indicate if our algorithm, not necessarily if it's accurate)


# Evaluate the performance of the Linear Regression algorithm by using the following four metrics
print('R^2:', metrics.score(y_test, y_pred))
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print("______________________________________\n")
