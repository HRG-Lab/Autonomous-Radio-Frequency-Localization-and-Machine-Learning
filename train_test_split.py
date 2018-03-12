import csv
import pandas as pd


## the data set we want to work with
filename = '/Users/etdel651/Documents/Classes /ECEN 403/output/shuffle_merge_header.csv'
data = pd.read_csv(filename)
print(data)

### make a subset of the data
### try taking in source, Length, RSSI, Tile number
feature_cols = ['Source', 'Length', 'RSSI', 'Tile number']

# use the list to select a subset of the original DataFrame
X = data[feature_cols]

# print the first 5 rows
print(X.head())

#check the type and shape of X
print (type(X))
print('this is the shape of x')
print (X.shape)



