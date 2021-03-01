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
from sklearn.metrics import f1_score
import warnings
warnings.filterwarnings("ignore")

Fsocrelis=list()
Precisionlis=list()
recalllis=list()
Accuracylis=list()

#database
MainDatabase = pd.read_excel("../database/MainDataset.xlsx")
# base on database we will set iloc
x = MainDatabase.iloc[:, :5].values  #independent variables
print(x)
y = MainDatabase.iloc[ : , -1].values #dependent variables
print(y)





#datauserate

thirtypercent=0.30  # training size 70%
fourtypercent=0.40   # training size 60%
fiftypercent=0.50    # training size 50%
sixtypercent=0.60    # training size 40%
seventypercent=0.70   # training size 30%


#knn

#naive bayes
print("\n########## Naive Bayes algorithm ###########")
gnb = GaussianNB()

X_train, X_test, y_train, y_test=train_test_split(x, y,test_size=thirtypercent, random_state=0)
gnb.fit(X_train, y_train)
#Predict the response for test dataset
y_pred = gnb.predict(X_test)
score=f1_score(y_test, y_pred, average='weighted')
print("test size=30, FScore = {0:.2f}".format(100*score),"%")


X_train, X_test, y_train, y_test=train_test_split(x, y,test_size=fourtypercent, random_state=0)
gnb.fit(X_train, y_train)
#Predict the response for test dataset
y_pred = gnb.predict(X_test)
score=f1_score(y_test, y_pred, average='weighted')
print("test size=40, FScore = {0:.2f}".format(100*score),"%")

X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=fiftypercent, random_state=0)
gnb.fit(X_train, y_train)
#Predict the response for test dataset
y_pred = gnb.predict(X_test)
score=f1_score(y_test, y_pred, average='weighted')
print("test size=50, FScore = {0:.2f}".format(100*score),"%")

X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=sixtypercent, random_state=0)
gnb.fit(X_train, y_train)
#Predict the response for test dataset
y_pred = gnb.predict(X_test)
score=f1_score(y_test, y_pred, average='weighted')
print("test size=60, FScore = {0:.2f}".format(100*score),"%")

X_train, X_test, y_train, y_test=train_test_split(x, y,test_size=seventypercent, random_state=0)
gnb.fit(X_train, y_train)
#Predict the response for test dataset
y_pred = gnb.predict(X_test)
score=f1_score(y_test, y_pred, average='weighted')
print("test size=70, FScore = {0:.2f}".format(100*score),"%")


print("\n########## SVM algorithm ###########")

clf = svm.SVC(kernel='linear') # Linear Kernel
X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=thirtypercent, random_state=0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
score=f1_score(y_test, y_pred, average='weighted')
print("test size=30, FScore = {0:.2f}".format(100*score),"%")

X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=fourtypercent, random_state=0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
score=f1_score(y_test, y_pred, average='weighted')
print("test size=40, FScore = {0:.2f}".format(100*score),"%")

X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=fiftypercent, random_state=0)
y_pred = clf.predict(X_test)
score=f1_score(y_test, y_pred, average='weighted')
print("test size=50, FScore = {0:.2f}".format(100*score),"%")


X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=sixtypercent, random_state=0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
score=f1_score(y_test, y_pred, average='weighted')
print("test size=60, FScore = {0:.2f}".format(100*score),"%")

X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=seventypercent, random_state=0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
score=f1_score(y_test, y_pred, average='weighted')
print("test size=70, FScore = {0:.2f}".format(100*score),"%")


print("\n########## Neural Network algorithm ###########")

mpl = MLPClassifier(max_iter=1000,alpha=1,random_state=0)
X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=thirtypercent, random_state=0)
mpl.fit(X_train, y_train)
y_pred = clf.predict(X_test)
score=f1_score(y_test, y_pred, average='weighted')
print("test size=30, FScore = {0:.2f}".format(100*score),"%")


X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=fourtypercent, random_state=0)
mpl.fit(X_train, y_train)
y_pred = clf.predict(X_test)
score=f1_score(y_test, y_pred, average='weighted')
print("test size=40, FScore = {0:.2f}".format(100*score),"%")


X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=fiftypercent, random_state=0)
mpl.fit(X_train, y_train)
y_pred = clf.predict(X_test)
score=f1_score(y_test, y_pred, average='weighted')
print("test size=50, FScore = {0:.2f}".format(100*score),"%")


X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=sixtypercent, random_state=0)
mpl.fit(X_train, y_train)
y_pred = clf.predict(X_test)
score=f1_score(y_test, y_pred, average='weighted')
print("test size=60, FScore = {0:.2f}".format(100*score),"%")

X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=seventypercent, random_state=0)
mpl.fit(X_train, y_train)
y_pred = clf.predict(X_test)
score=f1_score(y_test, y_pred, average='weighted')
print("test size=70, FScore = {0:.2f}".format(100*score),"%")

print("\n########## Random Forest Algorithm ###########")
X_train, X_test, y_train, y_test=train_test_split(x, y,test_size=thirtypercent, random_state=0)
clf=RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
score=f1_score(y_test, y_pred, average='weighted')
print("test size=30, FScore = {0:.2f}".format(100*score),"%")


X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=fourtypercent, random_state=0)
clf=RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
score=f1_score(y_test, y_pred, average='weighted')
print("test size=40, FScore = {0:.2f}".format(100*score),"%")


X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=fiftypercent, random_state=0)
clf=RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
score=f1_score(y_test, y_pred, average='weighted')
print("test size=50, FScore = {0:.2f}".format(100*score),"%")


X_train, X_test, y_train, y_test=train_test_split(x, y, test_size=sixtypercent, random_state=0)
clf=RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
score=f1_score(y_test, y_pred, average='weighted')
print("test size=60, FScore = {0:.2f}".format(100*score),"%")


X_train, X_test, y_train, y_test=train_test_split(x,y,test_size=seventypercent, random_state=0)
clf=RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
score=f1_score(y_test, y_pred, average='weighted')
print("test size=70, FScore = {0:.2f}".format(100*score),"%")