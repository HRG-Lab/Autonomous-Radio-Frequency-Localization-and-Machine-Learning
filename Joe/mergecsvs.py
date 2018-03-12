import os
from glob import glob
import pandas as pd
import csv


# this should be a for loop but i keep getting an error that I do not know how to get around yet
# delete the headers from the data before merging them
def delete_headers(datacollection = "/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection"):

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 0.csv", 'r') as infile, open("/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 0.csv", 'w') as outfile :
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 1.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 1.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 2.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 2.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
             # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 3.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 3.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 4.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 4.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 5.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 5.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 6.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 6.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
             # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 7.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 7.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 8.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 8.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 9.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 9.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 10.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 10.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 11.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 11.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 12.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 12.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 13.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 13.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
             # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 14.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 14.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 15.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 15.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
             # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 16.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 16.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
             # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 17.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 17.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
             # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 18.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 18.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 19.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 19.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 20.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 20.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 21.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 21.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 22.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 22.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 23.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 23.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
             # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 24.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 24.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 25.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 25.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 26.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 26.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 27.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 27.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 28.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 28.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
             # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 29.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 29.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 30.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 30.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 31.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 31.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
             # process each row
            writer.writerow(row)

    with open("/Users/etdel651/Documents/Classes /ECEN 403/First_Data_Collection/Tile 32.csv", 'r') as infile, open(
                "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers/Tile 32.csv", 'w') as outfile:
        reader = csv.reader(infile)
        next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        for row in reader:
            # process each row
            writer.writerow(row)


# I added an extra column to show where the data was taken
# This function takes in two arguments an input and an output file
def concatenate(indir = "/Users/etdel651/Documents/Classes /ECEN 403/output/no headers", outfile = "/Users/etdel651/Documents/Classes /ECEN 403/output/merge.csv" ):


#take in all the files in that directory that are csv files
    os.chdir(indir)   #current working directory
    fileList=glob("*.csv")    #take in all the csv files
    dfList = []       #empty list
    colnames = ["No.",	"Time",	"Source",	"Destination",	"Protocol",	"Length",	"Info",	"RSSI",	"Tile number"]
#print the filenames we want to merge

    for filename in fileList:
        print (filename)
        df=pd.read_csv(filename, header= None)
        dfList.append(df)

#output the file
    concatDf = pd.concat(dfList,axis=0)
    concatDf.columns = colnames
    concatDf.to_csv(outfile,index=None)



delete_headers()
#call the function to combine the files
concatenate()