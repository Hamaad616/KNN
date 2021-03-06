#!/usr/bin/env python
# coding: utf-8

# In[15]:


from sklearn import neighbors, datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd


iris = datasets.load_iris() 
#just printing the iris dataset
data1 = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                columns= iris['feature_names'] + ['target'])
print(data1)

X, y = iris.data[:, :], iris.target
Xtrain, Xtest, y_train, y_test = train_test_split(X, y, stratify = y, random_state = 0, train_size = 0.7)

scaler = preprocessing.StandardScaler().fit(Xtrain)
Xtrain = scaler.transform(Xtrain)
Xtest = scaler.transform(Xtest)

knn = neighbors.KNeighborsClassifier(n_neighbors=3)
knn.fit(Xtrain, y_train)
y_pred = knn.predict(Xtest)

print(accuracy_score(y_test, y_pred))
#print(classification_report(y_test, y_pred))
#print(confusion_matrix(y_test, y_pred))


# In[ ]:




