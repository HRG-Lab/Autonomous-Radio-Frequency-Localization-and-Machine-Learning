import csv
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

np.set_printoptions(precision=15,linewidth=105,threshold=34)

addressList = []

TEST_TRAIN_SET_NUMBER = 3 # This number corresponds to which testing/training data set needs to be analyzed

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
            rssiTrain[int(row[0])][addressIndex] = np.power(10,float(row[2])/10)
            rssiVarianceTrain[int(row[0])][addressIndex] = np.power(10,float(row[3])/10)
            addressCountTrain[int(row[0])][addressIndex] = row[4]
        rowNum += 1

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
        if rowNum != 0:
            addressIndex = addressList2.index(row[1])
            rssiTest[int(row[0])][addressIndex] = np.power(10,float(row[2])/10)
            rssiVarianceTest[int(row[0])][addressIndex] = np.power(10,float(row[3])/10)
            addressCountTest[int(row[0])][addressIndex] = row[4]
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
inBoth_Compressed = []

for i in range(len(inBoth)):
    try:
        if ((inBoth[i][:-3]) == (inBoth[i+1][:-3]) and (inBoth[i][:-3]) == (inBoth[i+2][:-3])):
            if (int(inBoth[i][-2:], 16) == int(inBoth[i+1][-2:],16) - 1) and (int(inBoth[i][-2:], 16) == int(inBoth[i+2][-2:],16) - 2):
                inBoth_Compressed.append(inBoth[i])
                i = i + 2
        else:
            inBoth_Compressed.append(inBoth[i])
    except IndexError:
        pass
print(len(inBoth_Compressed))

rssTrain = np.zeros((numPositions, len(inBoth)))
rssTest = np.zeros((numPositions, len(inBoth)))

# for i in range(numPositions):
#     for j in range(len(inBoth)):
#         position1 = addressList.index(inBoth[j])
#         position2 = addressList2.index(inBoth[j])
#         rssTrain[i][j] = rssiTrain[i][position1]
#         rssTest[i][j] = rssiTest[i][position2]


totalNumberMismatch = len(notInList1) + len(notInList2)
print("Total Number of Addresses in Training Set: ", numAddresses1)
print("Total Number of Addresses in Testing Set: ", numAddresses2)
print("Total Mismatch: ", totalNumberMismatch, sep='')
print("Total Match:", len(inBoth))
print("\nTotal Number of Data Points: ", np.sum(addressCountTest,axis=None))

# numPlots = np.ceil(np.sqrt(numAddresses))
# for plotNum in range(numAddresses):
#     plt.subplot(numPlots,numPlots,plotNum+1)

for i in range(numPositions):
    rssiTrain[i] = rssiTrain[i]/max(rssiTrain[i])
    rssiTest[i] = rssiTest[i]/max(rssiTest[i])

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

numPlots = np.ceil(np.sqrt(len(inBoth_Compressed)))
for i in range(len(inBoth_Compressed)):
    plt.subplot(numPlots, numPlots, i+1)
    indexNum1 = addressList.index(inBoth_Compressed[i])
    vector = rssiTrain[:,indexNum1]
    multiple = False
    try:
        indexNum2 = addressList.index(inBoth_Compressed[i][:-1]+str(int(inBoth_Compressed[i][-1:],16)+1))
        multiple = True
        vector = np.concatenate((vector, rssiTrain[:,indexNum2]),axis=1)
        print("After First Concatenation:")
        print(vector)
        indexNum3 = addressList.index(inBoth_Compressed[i][:-1]+str(int(inBoth_Compressed[i][-1:],16)+2))
        vector = np.concatenate((vector, rssiTrain[:,indexNum3]),axis=1)
    except ValueError:
        pass
    print(inBoth_Compressed[i])
    print(vector)
    if multiple:
        plt.plot(np.array(range(numPositions)),np.average(vector))
    else:
        plt.plot(np.array(range(numPositions)),vector)
    multiple = False

    indexNum1 = addressList2.index(inBoth_Compressed[i])
    vector = rssiTrain[:,indexNum1]
    try:
        indexNum2 = addressList2.index(inBoth_Compressed[i][:-1]+str(int(inBoth_Compressed[i][-1:],16)+1))
        multiple = True
        vector = np.concatenate((vector, rssiTest[:,indexNum2]),axis=1)
        indexNum3 = addressList2.index(inBoth_Compressed[i][:-1]+str(int(inBoth_Compressed[i][-1:],16)+2))
        vector = np.concatenate((vector, rssiTest[:,indexNum3]),axis=1)
    except ValueError:
        pass
    if multiple:
        plt.plot(np.array(range(numPositions)),np.average(vector))
    else:
        plt.plot(np.array(range(numPositions)),vector)

    plt.title(inBoth_Compressed[i])

# plt.subplot(1,2,1)
# plt.bar(np.arange(len(inBoth)),rssTrain[1], width=0.8)
# print(max(rssTrain[1]))
# print(min(rssTrain[1]))
# plt.ylim((0,max(rssTrain[1])))

# plt.subplot(1,2,2)
# plt.bar(np.arange(len(inBoth)),rssTest[1], width=0.8)

# plt.tight_layout()

plt.show()