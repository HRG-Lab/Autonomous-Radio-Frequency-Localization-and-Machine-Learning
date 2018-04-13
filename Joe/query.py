import csv
from numpy.random import randn
from pandas import DataFrame
import pandas as pd

filename = '/Users/etdel651/Documents/Classes /ECEN 403/output/shuffle_merge_header.csv'
data = pd.read_csv(filename, index_col = 0)
df = pd.DataFrame(data, columns = ['Source', 'Length', 'RSSI (dbm)'])
##print(df)
source1 = df['Source'] == 'ArubaNet_11:fc:f0'
source2 = source1.where
print(source2)

