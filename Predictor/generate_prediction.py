import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier


#database
MainDatabase = pd.read_excel(r'../database/MainDataset.xlsx')
# base on database we will set iloc
x = MainDatabase.iloc[:, :5].values  #independent variables
y = MainDatabase.iloc[ : , -1].values #dependent variables
print(y)

validationDataSet = pd.read_excel(r'../database/ValidationDataSet.xlsx')
# base on database we will set iloc
vX = validationDataSet.iloc[:, :5].values  #independent variables
vY = validationDataSet.iloc[ : , -1].values #dependent variables


X_train, X_test, y_train, y_test=train_test_split(x, y,test_size=0.40, random_state=0)
print(X_test)

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
y_pred=clf.predict(vX)
print(len(y_pred))

validationDataSet.to_excel(r'../database/predictedDataSet.xlsx', index=False)
validationDataSet.insert(6,"Prediction",y_pred,True)
validationDataSet.to_excel(r'../database/predictedDataSet.xlsx', index=False)

checkValidationDataSet = pd.read_excel(r'../database/predictedDataSet.xlsx')

print('Analysis Part')

real = checkValidationDataSet['Pneumonia (+ / -)'].values
predicted = checkValidationDataSet['Prediction'].values
print(real)
print(predicted)

print('real number of 1: ',real.tolist().count(1))
print('predicted number of 1: ',predicted.tolist().count(1))

