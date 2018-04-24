import csv
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

np.set_printoptions(precision=15,linewidth=105,threshold=34)
np.random.seed(2)

addressList = []

TEST_TRAIN_SET_NUMBER = 4 # This number corresponds to which testing/training data set needs to be analyzed

filename = 'TrainingSet' + str(TEST_TRAIN_SET_NUMBER) + '.csv'
print("Parsing file '", filename,"'",sep='')
with open(filename, 'r') as csvFile:
    hallData = csv.reader(csvFile, dialect='excel')
    rowNum = 0
    numAddresses1 = 10
    for row in hallData:
        if rowNum == 0:
            numPositions = int(row[6])
            numAddresses1 = int(row[8])
            rssiTrain = np.zeros((numPositions, numAddresses1))
            rssiVarianceTrain = np.zeros((numPositions, numAddresses1))
            addressCountTrain = np.zeros((numPositions, numAddresses1))
        elif rowNum <= numAddresses1:
            addressList.append(row[1])
        if rowNum != 0:
            addressIndex = addressList.index(row[1])
            rssiTrain[int(row[0])][addressIndex] = row[2] # np.power(10,float(row[2])/10)
            rssiVarianceTrain[int(row[0])][addressIndex] = row[3] # np.power(10,float(row[3])/10)
            addressCountTrain[int(row[0])][addressIndex] = row[4] # row[4]
        rowNum += 1

print(rssiTrain[1])

addressList2 = []
filename = 'TestingSet' + str(TEST_TRAIN_SET_NUMBER) + '.csv'
print("Parsing file '", filename,"'",sep='')
with open(filename, 'r') as csvFile:
    hallData = csv.reader(csvFile, dialect='excel')
    rowNum = 0
    # numAddresses = 10
    for row in hallData:
        if rowNum == 0:
            numPositions = int(row[6])
            numAddresses2 = int(row[8])
            rssiTest = np.zeros((numPositions, numAddresses2))
            rssiVarianceTest = np.zeros((numPositions, numAddresses2))
            addressCountTest = np.zeros((numPositions, numAddresses2))
        elif rowNum <= numAddresses2:
            addressList2.append(row[1])
            # print(row[1])
        # elif (float(row[2]) != -100) and (np.random.rand() < 0.1):
        #     print("Tile:", row[0])
        #     print("Address:", row[1])
        #     print("RSSI:", row[2], "\n")
        if rowNum != 0:
            addressIndex = addressList2.index(row[1])
            rssiTest[int(row[0])][addressIndex] = row[2] # np.power(10,float(row[2])/10)
            rssiVarianceTest[int(row[0])][addressIndex] = row[3] # np.power(10,float(row[3])/10)
            addressCountTest[int(row[0])][addressIndex] = row[4] # row[4]
        
        # except ValueError:
            # print(row[1], "not in list.")
        rowNum += 1

notInList1 = []
notInList2 = []
inBoth = []

for i in range(numAddresses1):
    try:
        addressList2.index(addressList[i])
        inBoth.append(addressList[i])
    except ValueError:
        notInList2.append(addressList[i])

for j in range(numAddresses2):
    try:
        addressList.index(addressList2[j])
    except ValueError:
        notInList1.append(addressList2[j])

print(inBoth)
inBoth = sorted(inBoth)

# for i in range(numPositions):
#     for j in range(len(inBoth)):
#         position1 = addressList.index(inBoth[j])
#         position2 = addressList2.index(inBoth[j])
#         rssTrain[i][j] = rssiTrain[i][position1]
#         rssTest[i][j] = rssiTest[i][position2]


totalNumberMismatch = len(notInList1) + len(notInList2)
print("Total Number of Addresses in Training Set: ", numAddresses1)
print("Total Number of Addresses in Testing Set: ", numAddresses2)
print("Total Number of Data Points: ", np.sum(addressCountTest,axis=None))
print("Total Mismatch: ", totalNumberMismatch, sep='')
print("Total Match:", len(inBoth))

# numPlots = np.ceil(np.sqrt(numAddresses))
# for plotNum in range(numAddresses):
#     plt.subplot(numPlots,numPlots,plotNum+1)

# rssTrain = np.zeros((numPositions, len(inBoth)))
# rssTest = np.zeros((numPositions, len(inBoth)))

for i in range(numAddresses1):
    factor = max([rssiTrain[k][i] for k in range(numPositions)])
    print("Factor:",factor)
    for j in range(numPositions):
        if rssiTrain[j][i] != -100:
            rssiTrain[j][i] = rssiTrain[j][i]-factor

for i in range(numAddresses2):
    factor = max([rssiTest[k][i] for k in range(numPositions)])
    for j in range(numPositions):
        if rssiTest[j][i] != -100:
            rssiTest[j][i] = rssiTest[j][i]-factor

# with open('AddressList.csv','w',newline='') as csvFile:
#     author = csv.writer(csvFile)
#     for address in inBoth:
#         author.writerow([address])

# with open("DataAnalysisFile.csv",'w',newline='') as csvFile:
#     author = csv.writer(csvFile)
#     for i in range(numPositions):
#         for j in range(numAddresses):
#             author.writerow([addressList[j],rssiTrain[i][j], rssiTest[i][j]])
    
# print("Tile ", i, ": ", np.sqrt(np.sum(np.power(rssiTrain-rssiTest[i],2),axis=1)),sep='')

numPlots = np.ceil(np.sqrt(len(inBoth)))
for i in range(len(inBoth)):
    plt.subplot(numPlots, numPlots, i+1)
    indexNum1 = addressList.index(inBoth[i])
    print("indexNum1:", indexNum1)
    indexNum2 = addressList2.index(inBoth[i])
    plt.plot(range(numPositions),[rssiTrain[j][indexNum1] for j in range(numPositions)],label=inBoth[i])
    plt.plot(range(numPositions),[rssiTest[j][indexNum2] for j in range(numPositions)])
    plt.title(inBoth[i])



# plt.subplot(1,2,1)
# plt.bar(np.arange(len(inBoth)),rssTrain[1], width=0.8)
# print(max(rssTrain[1]))
# print(min(rssTrain[1]))
# plt.ylim((0,max(rssTrain[1])))

# plt.subplot(1,2,2)
# plt.bar(np.arange(len(inBoth)),rssTest[1], width=0.8)


plt.show()