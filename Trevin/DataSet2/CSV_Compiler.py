import csv
import numpy as np
import matplotlib.pyplot as plt
import math

# Number of positions marked off along the hallway
NUM_POSITIONS = 33

# Configure print options
np.set_printoptions(precision=1,linewidth=94,threshold=10)

# Initialize the lists to store the address, signal strengths, and counts in
addressList = []
signalStrengths = [[] for i in range(NUM_POSITIONS)]
addressCount = [[] for i in range(NUM_POSITIONS)]

# Parameters for CSV to generate
generateCSV = True
training = False    # Set this to True to use the first 2/3 to make training set, false to use last 1/3 for testing set
TEST_TRAIN_SET_NUMBER = 3

###### MEAN ######

for tile in range(NUM_POSITIONS):
    filename = 'Tile ' + str(tile) + '.csv'
    print("Parsing file '", filename,"'",sep='')
    with open(filename,mode='r') as csvData:
        hallData = csv.reader(csvData, dialect='excel')
        rowNum = 0
        nextRow = False
        numLines = 0
        for row in hallData:
            numLines += 1
            address = row[2]
            signalStrength = row[7]
            if signalStrength == '': # or ('ArubaNet' not in address):
                nextRow = True
            if nextRow == False and rowNum > 0:
                try:
                    val = addressList.index(address)
                except ValueError:
                    addressList.append(address)
            nextRow = False
            rowNum += 1
        # print("There are ", numLines, " data entries.")
    
    signalStrengths[tile] = [0 for i in addressList]
    addressCount[tile] = [0 for i in addressList]

    with open(filename,mode='r') as csvData:
        hallData = csv.reader(csvData, dialect='excel')
        rowNum = 0
        for row in hallData:
            if rowNum==0:
                header = row
            elif ((training == True) and (rowNum < (2.0/3)*numLines)) or ((training == False)):# and (rowNum >= (2.0/3)*numLines)):
                address = row[2]
                signalStrength = row[7]
                if signalStrength.endswith(' dBm'):
                    signalStrength = int(signalStrength[:-4])
                if signalStrength=='': # or ('ArubaNet' not in address):
                    nextRow = True
                if nextRow == False:
                    # try:
                    position = addressList.index(address)
                    signalStrengths[tile][position] += signalStrength
                    addressCount[tile][position] += 1
                    # except ValueError:
                    #     addressList.append(address[:-3])
                    #     signalStrengths[tile].append(signalStrength)
                    #     addressCount[tile].append(1)
            nextRow = False
            rowNum += 1
        # Divide the signal strengths by number observed to get the average strength for that address
        signalStrengths[tile] = [x/y if y!=0 else 0 for x,y in zip(signalStrengths[tile],addressCount[tile])]

numAddresses = len(addressList)
print("Number of Addresses: ", numAddresses)
print("Number of Data Points: ", sum(np.sum(addressCount)))
varianceMatrix = np.zeros((NUM_POSITIONS, numAddresses))
# varianceAddressCount = np.zeros((NUM_POSITIONS numAddresses)

###### VARIANCE ######

for tile in range(NUM_POSITIONS):
    filename = 'Tile ' + str(tile) + '.csv'
    print("Re-parsing file '", filename,"'",sep='')
    with open(filename,mode='r') as csvData:
        hallData = csv.reader(csvData, dialect='excel')
        numLines = sum(1 for line in hallData)
    with open(filename,mode='r') as csvData:
        hallData = csv.reader(csvData, dialect='excel')
        rowNum = 0
        for row in hallData:
            if rowNum==0:
                header = row
            elif ((training == True) and (rowNum < (2.0/3)*numLines)) or ((training == False)):# and (rowNum >= (2.0/3)*numLines)):
                address = row[2]
                signalStrength = row[7]
                if signalStrength.endswith(' dBm'):
                    signalStrength = int(signalStrength[:-4])
                if signalStrength=='' or ('ArubaNet' not in address):
                    nextRow = True
                if nextRow == False:
                    try:
                        position = addressList.index(address)
                        varianceMatrix[tile][position] += np.power(signalStrength-signalStrengths[tile][position],2)
                        # varianceAddressCount[position] += 1
                    except IndexError:
                        print("Tile: ", tile)
                        print("Position: ", position)
                        quit()
            nextRow = False
            rowNum += 1
        varianceMatrix[tile][0:len(addressCount[tile])] = [x/y if y!=0 else 0 for x,y in zip(varianceMatrix[tile],addressCount[tile])]

# Go back and put in -100dBm for all of the addresses with frames not observed at each location
numAddresses = len(addressList)
for i in range(len(signalStrengths)):
    for j in range(len(signalStrengths[i])):
        if signalStrengths[i][j] == 0:
            signalStrengths[i][j] = -1000
    while len(signalStrengths[i]) < numAddresses:
        signalStrengths[i].append(-1000)
        addressCount[i].append(0)

# This will print the number of frames recieved from each address at the locations listed
# for location in [0, 10, 21, 32]:
#     print("Stations observed at location ", location, ":\n", addressCount[location])

for i in range(numAddresses):
    factor = max([signalStrengths[j][i] for j in range(NUM_POSITIONS)])
    for j in range(NUM_POSITIONS):
        if signalStrengths[j][i]==-1000:
            signalStrengths[j][i] =-100
        # else:
        #     signalStrengths[j][i] -= factor

if (generateCSV):
    if (training == True):
        outfile = 'TrainingSet' + str(TEST_TRAIN_SET_NUMBER) + '.csv'
    else:
        outfile = 'TestingSet' + str(TEST_TRAIN_SET_NUMBER) + '.csv'
    with open(outfile,mode='w', newline='') as csvFile:
        dataWriter = csv.writer(csvFile, dialect='excel')
        dataWriter.writerow(['Tile', 'Address', 'Average dBm', 'Variance in dBm', 'Address Count', 'Number of Positions', NUM_POSITIONS, 'Number of Addresses', numAddresses])
        for tile in range(NUM_POSITIONS):
            for addr in range(numAddresses):
                dataWriter.writerow([tile, addressList[addr], signalStrengths[tile][addr], varianceMatrix[tile][addr], addressCount[tile][addr]])
