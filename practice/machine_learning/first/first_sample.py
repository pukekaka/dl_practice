import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

iris_data = pd.read_csv(os.getcwd()+'\\first\\iris.csv')
iris_mydata = iris_data.drop('Id', axis=1)

sb = sns.pairplot(iris_mydata)
plt.show()

#print(iris_data.keys())
#iris_data.columns =['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm','Species']
#iris_data.columns = iris_data.keys()
#iris_exceptid_data = iris_data.drop(['Id'])

#print(iris_data['Id'])

#iris_mydata2 = iris_data.drop(0, axis=0)

#print(iris_data.shape)
#print(iris_mydata.shape)
#print(iris_mydata2.shape)


#plt.figure()
#plt.savefig(sb)