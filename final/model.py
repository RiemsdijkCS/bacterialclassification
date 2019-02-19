import pandas as pd 
from sklearn.model_selection import LeaveOneOut
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('model_2.csv')

#Probleem waar ik tegen aan loop, hoe geef ik mijn target en data met pandas
X = data.iloc[:,0:11]
y = data.loc[:,'Diagnosis']

loo = LeaveOneOut()

print(X)
print(y)





for train_index, test_index in loo.split(X): # Split in X
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)


# model = LogisticRegression()

# model.fit(X_train, y_train)
# z = model.score(X_test, y_test)

# print(z)



