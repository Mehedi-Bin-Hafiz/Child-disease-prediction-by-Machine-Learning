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
from sklearn.metrics import confusion_matrix


checkValidationDataSet = pd.read_excel(r'../database/predictedDataSet.xlsx')


real = checkValidationDataSet['Disease'].values
predicted = checkValidationDataSet['Prediction'].values


tn, fp, fn, tp = confusion_matrix(real,predicted).ravel()
print('tn :',tn)
print('fp :',fp)
print('fn :',fn)
print('tp :',tp)
print("Total sample: ",len(real))
print(tn, fp, fn, tp)