import csv
import pandas as pd
import numpy as nd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as nd
import matplotlib.pyplot as plt

filename = '/Users/etdel651/Documents/Classes /ECEN 403/output/shuffle_merge_header.csv'
data = pd.read_csv(filename, index_col = 0)
print(data)
size_mapping = {'ArubaNet_11:f1:41': 3, 'ArubaNet_11:f1:40':4, 'ArubaNet_11:fd:b2':5, 'ArubaNet_11:eb:c1': 6,
                'ArubaNet_11: f1:42': 7, 'ArubaNet_11:f9:42':8, 'ArubaNet_11:ef:70': 8, 'ArubaNet_11:ef:71': 9, 'ArubaNet_11:ef:72':10, 'ArubaNet_11:fc:f0': 11,
                'ArubaNet_11: fc:f1': 12, 'ArubaNet_11:fc:f2': 13, 'ArubaNet_11:fd:b0': 14, 'ArubaNet_31:ef:71': 15, 'ArubaNet_11:eb:b0': 16, 'ArubaNet_11:eb:b1': 17,
               'ArubaNet_11:fa:d0':18, 'ArubaNet_11:fa:d1': 19, 'ArubaNet_11:fa:d2': 20, 'ArubaNet_11:ec:f0': 21, 'ArubaNet_11:ec:f1': 22, 'ArubaNet_11:ec:f2': 23,
                'ArubaNet_11: f9:70': 24, 'ArubaNet_11:f9:71': 25, 'ArubaNet_11:f9:72': 26, 'ArubaNet_11:eb:b2': 27, 'ArubaNet_11:ec:e1':28 }
data['Source'] = data['Source'].map(size_mapping)
data = data.dropna()
print(data)





feature_cols = ['Source', 'RSSI (dbm)']
# use the list to select a subset of the original DataFrame
X = data[feature_cols]

#select a series from the dataFrame
y = data['Tile number']

# split the set
X_train,X_test,y_train,y_test = train_test_split(X, y, random_state = 1)

# try k=1 through k=25 and record testing accuracy
k_range = range(1,200)
scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X_train,y_train)
    y_pred = knn.predict(X_test)
    scores.append(metrics.accuracy_score(y_test, y_pred))

#plot therelationship between K and testing accuracy
plt.plot(k_range, scores)
plt.xlabel('Value of k for KNN')
plt.ylabel('Testing Accuracy')
plt.show()

# instantiate learning model (k = 3)
knn = KNeighborsClassifier(n_neighbors=3)

# fitting the model
knn.fit(X_train, y_train)

# predict the response
pred = knn.predict(X_test)

# evaluate accuracy
print (metrics.accuracy_score(y_test, pred))



