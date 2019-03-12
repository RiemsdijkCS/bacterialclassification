import pandas as pd 
from sklearn.model_selection import LeaveOneOut
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.dummy import DummyClassifier
data = pd.read_csv('model_3.csv')
model = LogisticRegression(solver='liblinear', multi_class='ovr', class_weight='balanced')
loo = LeaveOneOut()
neigh = KNeighborsClassifier(n_neighbors=10)
clf = GaussianNB()
dummy = DummyClassifier()


X = data.iloc[:,0:12].to_numpy()
y = data.loc[:,'Diagnosis'].to_numpy()



for train_index, test_index in loo.split(X): # Split in X
    # print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(y_pred, y_test)
    


score = cross_val_score(clf,X,y, cv=loo.split(X))
print(sum(score)/len(score) *100.0, '%')




