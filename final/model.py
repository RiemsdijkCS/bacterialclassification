import pandas as pd 
from sklearn.model_selection import LeaveOneOut
from sklearn.linear_model import LogisticRegression

data = pd.read_csv('model.csv')

loo = LeaveOneOut()

for train_index, test_index in loo.split(data):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = data[train_index], data[test_index]
    y_train, y_test = data[train_index], data[test_index]
    print(X_train, X_test, y_train, y_test)


model = LogisticRegression()

model.fit(X_train, y_train)






