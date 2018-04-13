import csv
import pandas as pd
import numpy as nd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score


## the data set we want to work with
filename = '/Users/etdel651/Documents/Classes /ECEN 403/output/shuffle_merge_header.csv'
data = pd.read_csv(filename, index_col = 0)
## delete the dbm from each cell
data['RSSI (dbm)'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')
### write the change to the file
data.to_csv(filename)
#print the first 5 rows
print(data.head())

#print the last 5 rows
print(data.tail())



## make a subset of the data
## try taking in source, Length, RSSI, Tile number
feature_cols = ['Source', 'Length', 'RSSI (dbm)']

# use the list to select a subset of the original DataFrame
X = data[feature_cols]

# print the first 5 rows
print(X.head())

#check the type and shape of X
print (type(X))
print('this is the shape of x')
print (X.shape)

#select a series from the dataFrame
y = data['Tile number']


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X, y, random_state = 1)

#default split is 75% for training and 25% for testing
print('Split the data set into train and test')
print (X_train.shape)
print (y_train.shape)
print (X_test.shape)
print (y_test.shape)


##this is just a place holder for the correct syntax that we need
#import seaborn as sns
#sns.pairplot(data, x_vars=['RSSI (dbm)'],y_vars='Tile number', size=7, aspect=0.7, kind='reg')
#plt.show()




















