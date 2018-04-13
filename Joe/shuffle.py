import random
import csv
import pandas as pd

#fid = open("/Users/etdel651/Documents/Classes /ECEN 403/output/merge.csv", "r")
#li = merged.readlines()
#fid.close()
#print(li)

#random.shuffle(li)
#print(li)



#fid = open("/Users/etdel651/Documents/Classes /ECEN 403/output/shuffle_merge.csv", "w")
#fid.writelines(li)
#fid.close()

# remove the header of the merged file
with open("/Users/etdel651/Documents/Classes /ECEN 403/output/merge.csv", 'r') as infile, open(
        "/Users/etdel651/Documents/Classes /ECEN 403/output/merge_nohead.csv", 'w') as outfile:
    reader = csv.reader(infile)
    next(reader, None)  # skip the headers
    writer = csv.writer(outfile)
    for row in reader:
        # process each row
        writer.writerow(row)

#randomize the data so when we split it we have half the data points from each point 
fid = open("/Users/etdel651/Documents/Classes /ECEN 403/output/merge_nohead.csv", "r")
li = fid.readlines()
fid.close()
print(li)

random.shuffle(li)
print(li)



fid = open("/Users/etdel651/Documents/Classes /ECEN 403/output/shuffle_merge.csv", "w")
fid.writelines(li)
fid.close()

###add a header so we know what columns are what
df = pd.read_csv("/Users/etdel651/Documents/Classes /ECEN 403/output/shuffle_merge.csv", header = None)
df.columns = ["No.",	"Time",	"Source",	"Destination",	"Protocol",	"Length",	"Info",	"RSSI (dbm)",	"Tile number"]
df.to_csv("/Users/etdel651/Documents/Classes /ECEN 403/output/shuffle_merge_header.csv")


