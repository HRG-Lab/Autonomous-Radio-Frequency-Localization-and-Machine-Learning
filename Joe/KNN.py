import csv
import pandas as pd
import numpy as nd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as nd
import matplotlib.pyplot as plt



filename = '/Users/etdel651/Documents/Classes /ECEN 403/Datasets/rssi.csv'
data = pd.read_csv(filename, index_col = 0)
#print(data)
print(data)

feature_cols = ['ap', 'signal']
# use the list to select a subset of the original DataFrame
X = data[feature_cols]

#select a series from the dataFrame
y = data['x','y','z']

