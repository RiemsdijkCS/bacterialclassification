import pandas as pd 
from sklearn.model_selection import LeaveOneOut
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import metrics

data = pd.read_csv('model_3.csv')

#Probleem waar ik tegen aan loop, hoe geef ik mijn target en data met pandas
X = data.iloc[:, 0:11].to_numpy()
y = data.loc[:, 'Diagnosis'].to_numpy()

model = LogisticRegression(solver='liblinear', multi_class='ovr')
loo = LeaveOneOut()


for train_index, test_index in loo.split(X): # Split in X
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    # print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(y_test, y_pred)

    
print(metrics.accuracy_score(y_test, y_pred))
    

  




