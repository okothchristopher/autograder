

# importing the libraries
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from sklearn import datasets

raw_data = datasets.load_iris()
data = pd.DataFrame(raw_data["data"], columns=raw_data["feature_names"])
data.loc[:, "class"] = raw_data["target"]

X = data.drop(columns=['class'])
y = data['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4)

train = X_train.copy()
train['class'] = y_train
# train.to_csv('iris_train.csv',index=False)

# X_test.to_csv('iris_test.csv')
# y_test.to_csv('iris_test_solutions.csv')

from sklearn.linear_model import LogisticRegression
logreg=LogisticRegression()
logreg.fit(X_train,y_train)
y_pred=logreg.predict(X_test)

from sklearn import metrics
print(metrics.accuracy_score(y_test,y_pred))
