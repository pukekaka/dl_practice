import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import seaborn as sns
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

load_boston_housing = load_boston()

boston_housing = pd.read_csv(os.getcwd()+'\\boston.csv')
boston_housing_s = pd.DataFrame(load_boston_housing.data, columns=load_boston_housing.feature_names)
boston_housing_t = pd.DataFrame(load_boston_housing.target, columns = ['PRICE'])

#print(boston_housing_s.head())
#print(boston_housing_t.head())

X_train, X_test, Y_train, Y_test = train_test_split(boston_housing_s, boston_housing_t, random_state=5)

print(X_train.shape)
print(X_test.shape)

print(Y_train.shape)
print(Y_test.shape)


linear_model = LinearRegression()
linear_model.fit(X_train, Y_train)

print('coeff_: {}'.format(linear_model.coef_))
print('intercept_: {}'.format(linear_model.intercept_))

Y_prediction = linear_model.predict(X_test)

plt.scatter(Y_test, Y_prediction)
plt.xlabel('real price')
plt.ylabel('predict price')
plt.title('real vs predict relation')
sb = sns.pairplot(boston_housing)
plt.show()




#plt.show()

#print(boston_housing.columns)
#print(boston_housing_s.columns)