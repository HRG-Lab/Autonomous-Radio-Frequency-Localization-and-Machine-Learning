import csv
import pandas as pd
import numpy as nd
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt



## the data set we want to work with
filename = '/Users/etdel651/Documents/Classes /ECEN 403/output/shuffle_merge_header.csv'
data = pd.read_csv(filename, index_col = 0)

## filter the data based on the wifi source
data_filtered1 = data[(data.Source == 'ArubaNet_11:ef:71')]
print(data_filtered1)

import seaborn as sns
sns.pairplot(data_filtered1, x_vars=['RSSI (dbm)'],y_vars='Tile number', size=7, aspect=0.7, kind='reg')
plt.title('ArubaNet_11:ef:71', fontsize=8)
plt.show()

## RSSI data in dbm
## not sure if we need source or info to compare with
## Graph all the data and talk about it next week at the meeting
## this will help us determine what ML algorithm to use and what features to bring in

