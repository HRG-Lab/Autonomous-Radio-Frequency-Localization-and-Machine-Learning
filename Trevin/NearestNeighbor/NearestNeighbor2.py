import csv
import numpy as np
import math
import matplotlib.pyplot as plt

np.set_printoptions(precision=1,linewidth=150,threshold=34)

addressList = []

filename = 'TrainingSet1.csv'
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
            rssiTrain[int(row[0])][addressIndex] = row[2]
            rssiVarianceTrain[int(row[0])][addressIndex] = row[3]
            addressCountTrain[int(row[0])][addressIndex] = row[4]
        rowNum += 1

filename = 'TestingSet1.csv'
print("Parsing file '", filename,"'",sep='')
with open(filename, 'r') as csvFile:
    hallData = csv.reader(csvFile, dialect='excel')
    rowNum = 0
    numAddresses = 10
    for row in hallData:
        if rowNum == 0:
            numPositions = int(row[6])
            numAddresses = int(row[8])
            rssiTest = np.zeros((numPositions, numAddresses))
            rssiVarianceTest = np.zeros((numPositions, numAddresses))
            addressCountTest = np.zeros((numPositions, numAddresses))
        else:
            addressIndex = addressList.index(row[1])
            rssiTest[int(row[0])][addressIndex] = row[2]
            rssiVarianceTest[int(row[0])][addressIndex] = row[3]
            addressCountTest[int(row[0])][addressIndex] = row[4]
        rowNum += 1

# print(rssiVarianceTest)
plotTracker = [False for addr in range(numAddresses)]
for addr in range(numAddresses):
    plotTracker[addr] = max([addressCountTrain[j][addr]+addressCountTest[j][addr] for j in range(numPositions)]) > 500

plt.subplot(1,2,1)
for addr in range(numAddresses):
    if (plotTracker[addr]):
        plt.errorbar(range(numPositions),[rssiTrain[j][addr] for j in range(numPositions)],
                     yerr=[np.sqrt(rssiVarianceTrain[j][addr]) for j in range(numPositions)], 
                     label=addressList[addr], elinewidth=0.5, capsize=3)

plt.title("Train Data")
plt.ylabel("Signal Power (dBm)")
plt.xlabel("Hallway Position (tile number)")
# plt.legend(loc='upper left')

plt.subplot(1,2,2)
for addr in range(numAddresses):
    if (plotTracker[addr]):
        plt.errorbar(range(numPositions),[rssiTest[j][addr] for j in range(numPositions)],
                     yerr=[np.sqrt(rssiVarianceTest[j][addr]) for j in range(numPositions)], 
                     label=addressList[addr], elinewidth=0.5, capsize=3)


plt.title("Test Data")
plt.ylabel("Signal Power (dBm)")
plt.xlabel("Hallway Position (tile number)")
# plt.legend(loc='upper left')

print ('(True Location, Nearest Neighbor Location)')
error = 0
for i in range(numPositions):
    # print(np.multiply(rssiTrain,rssiTest[i]))
    innerProductVector = np.sum(np.power(np.add(rssiTrain,-rssiTest[i]),2),axis=1)
    # print(innerProductVector)
    closest = np.argmin(innerProductVector)
    minVal = np.min(innerProductVector)
    error += abs(i-closest)
    print('(', i, ',', closest, ') -- ', minVal)
print("Average error:", error/numPositions)

plt.show()