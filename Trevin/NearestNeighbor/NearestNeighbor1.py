import csv
import numpy as np
import math
import matplotlib.pyplot as plt

np.set_printoptions(precision=15,linewidth=105,threshold=34)

addressList = []

TEST_TRAIN_SET_NUMBER = 3 # This number corresponds to which testing/training data set needs to be analyzed

filename = 'TrainingSet' + str(TEST_TRAIN_SET_NUMBER) + '.csv'
print("Parsing file '", filename,"'",sep='')
with open(filename, 'r') as csvFile:
    hallData = csv.reader(csvFile, dialect='excel')
    rowNum = 0
    numAddresses = 10
    for row in hallData:
        if rowNum == 0:
            numPositions = int(row[6])
            numAddresses = int(row[8])
            rssiTrain = np.zeros((numPositions, numAddresses))
            rssiVarianceTrain = np.zeros((numPositions, numAddresses))
            addressCountTrain = np.zeros((numPositions, numAddresses))
        elif rowNum <= numAddresses:
            addressList.append(row[1])
        if rowNum != 0:
            addressIndex = addressList.index(row[1])
            rssiTrain[int(row[0])][addressIndex] = np.power(10,float(row[2])/10)
            rssiVarianceTrain[int(row[0])][addressIndex] = np.power(10,float(row[3])/10)
            addressCountTrain[int(row[0])][addressIndex] = row[4]
        rowNum += 1

filename = 'TestingSet' + str(TEST_TRAIN_SET_NUMBER) + '.csv'
print("Parsing file '", filename,"'",sep='')
with open(filename, 'r') as csvFile:
    hallData = csv.reader(csvFile, dialect='excel')
    rowNum = 0
    # numAddresses = 10
    for row in hallData:
        if rowNum == 0:
            numPositions = int(row[6])
            # numAddresses = int(row[8])
            rssiTest = np.multiply(np.ones((numPositions, numAddresses)),0)
            rssiVarianceTest = np.zeros((numPositions, numAddresses))
            addressCountTest = np.zeros((numPositions, numAddresses))
        else:
            try:
                addressIndex = addressList.index(row[1])
                rssiTest[int(row[0])][addressIndex] = np.power(10,float(row[2])/10)
                rssiVarianceTest[int(row[0])][addressIndex] = np.power(10,float(row[3])/10)
                addressCountTest[int(row[0])][addressIndex] = row[4]
            except ValueError:
                print(row[1], "not in list.")
        rowNum += 1

# print(rssiVarianceTest)
plotTracker = [False for addr in range(numAddresses)]
for addr in range(numAddresses):
    plotTracker[addr] = (addressList[addr] == 'ArubaNet_11:ef:72') or (addressList[addr] == 'ArubaNet_10:e0:42')# max([addressCountTrain[j][addr]+addressCountTest[j][addr] for j in range(numPositions)]) > 500

# for position in range(numPositions):
#     trainMagnitude = np.sqrt(sum(np.power(rssiTrain[position],2)))
#     rssiTrain[position] = rssiTrain[position]/trainMagnitude
#     rssiVarianceTrain[position] = rssiVarianceTrain[position]/np.power(trainMagnitude,2)
#     testMagnitude = np.sqrt(sum(np.power(rssiTest[position],2)))
#     rssiTest[position] = rssiTest[position]/testMagnitude
#     rssiVarianceTest[position] = rssiVarianceTest[position]/np.power(testMagnitude,2)

for i in range(numPositions):
    rssiTrain[i] = rssiTrain[i]/np.linalg.norm(rssiTrain[i])
    rssiTest[i] = rssiTest[i]/np.linalg.norm(rssiTest[i])
    print("Tile ", i, ": ", np.dot(rssiTrain[i],rssiTest[i]),sep='')


# print(rssiVarianceTest)
plt.subplot(1,2,1)
for addr in range(numAddresses):
    if (max([addressCountTrain[j][addr] for j in range(numPositions)]) > 1000):
        plt.errorbar(range(numPositions),[rssiTrain[j][addr] for j in range(numPositions)],
                     yerr=[np.sqrt(rssiVarianceTrain[j][addr]) for j in range(numPositions)], 
                     label=addressList[addr], elinewidth=0.5, capsize=3)

plt.subplot(1,2,2)
for addr in range(numAddresses):
    if (max([addressCountTest[j][addr] for j in range(numPositions)]) > 500):
        plt.errorbar(range(numPositions),[rssiTest[j][addr] for j in range(numPositions)],
                     yerr=[np.sqrt(rssiVarianceTest[j][addr]) for j in range(numPositions)], 
                     label=addressList[addr], elinewidth=0.5, capsize=3)


plt.title("Signal Powers Across Hallway")
plt.ylabel("Signal Power (mW)")
plt.xlabel("Hallway Position (tile number)")
plt.legend(loc='lower left')

error = 0
print ('(True Location, Nearest Neighbor Location)')
for i in range(numPositions):
    innerProductVector = np.zeros(numPositions)
    for j in range(numPositions):
        innerProductVector[j] = np.dot(rssiTest[i],rssiTrain[j])
    print("Tile ", i, ": ", innerProductVector, sep='')
    # print(innerProductVector)
    closest = np.argmax(innerProductVector)
    maxVal = np.max(innerProductVector)
    error += np.power(i-closest,2)
    print('(', i, ',', closest, ') -- ', maxVal)
print("Average Error: ", np.sqrt(error/numPositions), sep='')

# plt.show()