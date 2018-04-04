import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math

# Number of positions marked off along the hallway
NUM_FILES = 2

# Configure print options
np.set_printoptions(precision=1,linewidth=94,threshold=10)

# Initialize the lists to store the source, signal strengths, and counts in
sourceList = []
signalMatrix = [[]]
sourceCount = [[]]
varianceMatrix = [[]]

# Pull in the data from the nth csv file and put sources into sourceList, signal strengths
# into the nth column of signalMatrix, and number of frames from that source into sourceCount

def importDataSet(filename, isFirst=False):
    if (isFirst):
        dataSetIndex = 0
    else:
        dataSetIndex = len(signalMatrix)

    ###### AVERAGE ######
    print("Parsing file '", filename,"'",sep='')
    with open(filename,mode='r') as csvData:
        location1_Data = csv.reader(csvData, dialect='excel')
        rowNum = 0
        nextRow = False
        numLines = 0
        for row in location1_Data:
            if rowNum != 0:
                numLines += 1
                source = row[2]
                signalStrength = row[4][:-7]
                protocolName = row[5]
                if signalStrength == '' or protocolName != "WiFi":
                    nextRow = True
                if nextRow == False and rowNum > 0:
                    try:
                        val = sourceList.index(source)
                    except ValueError:
                        sourceList.append(source)
            nextRow = False
            rowNum += 1
        # print("There are ", numLines, " data entries.")
    
    if(isFirst):
        signalMatrix[0] = [0 for i in sourceList]
        sourceCount[0] = [0 for i in sourceList]
        varianceMatrix[0] = [0 for i in sourceList]
    else:
        signalMatrix.append([0 for i in sourceList])
        sourceCount.append([0 for i in sourceList])
        varianceMatrix.append([0 for i in sourceList])

    with open(filename,mode='r') as csvData:
        location1_Data = csv.reader(csvData, dialect='excel')
        rowNum = 0
        for row in location1_Data:
            if rowNum==0:
                header = row
            else:
                source = row[2]
                signalStrength = row[4]
                protocolName = row[5]
                if signalStrength=='' or protocolName != "WiFi":
                    nextRow = True
                else:
                    signalStrength = int(signalStrength[:-7])
                if nextRow == False:
                    try:
                        sourceIndex = sourceList.index(source)
                        signalMatrix[dataSetIndex][sourceIndex] += signalStrength
                        sourceCount[dataSetIndex][sourceIndex] += 1
                    except IndexError:
                        print(dataSetIndex, ", ", sourceIndex, sep='')
                        print(signalMatrix)
                        print("Quitting.")
                        quit()
                    # except ValueError:
                    #     sourceList.append(source[:-3])
                    #     signalMatrix[dataSetIndex].append(signalStrength)
                    #     sourceCount[dataSetIndex].append(1)
            nextRow = False
            rowNum += 1
        # Divide the signal strengths by number observed to get the average strength for that source
        signalMatrix[dataSetIndex] = [x/y if y!=0 else 0 for x,y in zip(signalMatrix[dataSetIndex],sourceCount[dataSetIndex])]

    ###### VARIANCE ######

    print("Re-parsing file '", filename,"'",sep='')
    with open(filename,mode='r') as csvData:
        hallData = csv.reader(csvData, dialect='excel')
        rowNum = 0
        for row in hallData:
            if rowNum==0:
                header = row
            else:
                source = row[2]
                signalStrength = row[4]
                protocolName = row[5]
                if signalStrength=='' or protocolName != "WiFi":
                    nextRow = True
                else:
                    signalStrength = int(signalStrength[:-7])
                if nextRow == False:
                    try:
                        sourceIndex = sourceList.index(source)
                        varianceMatrix[dataSetIndex][sourceIndex] += np.power(signalStrength-signalMatrix[dataSetIndex][sourceIndex],2)
                        # variancesourceCount[sourceIndex] += 1
                    except IndexError:
                        print(varianceMatrix)
                        print("dataSetIndex: ", dataSetIndex)
                        print("Source:", source)
                        print("Position: ", sourceIndex)
                        quit()
            nextRow = False
            rowNum += 1
        varianceMatrix[dataSetIndex][0:len(sourceCount[dataSetIndex])] = [x/y if y!=0 else 0 for x,y in zip(varianceMatrix[dataSetIndex],sourceCount[dataSetIndex])]

# importDataSet('Room154_Set1.csv', isFirst=True)
# importDataSet('Room154_Set2.csv')
# importDataSet('Room164_Set1.csv')
# importDataSet('Room164_Set2.csv')
importDataSet('Room167_Set1.csv', isFirst=True)
importDataSet('Room167_Set2.csv')

numsources = len(sourceList)
print("Number of Sources:", numsources)

# Go back and put in 0dBm for all of the sources with frames not observed at each location
for i in range(len(signalMatrix)):
    while len(signalMatrix[i]) < numsources:
        signalMatrix[i].append(0)
        sourceCount[i].append(0)

# plotTracker = [False for i in sourceList]
# for i in range(numsources):
#     indicator = np.prod(np.array([signalMatrix[j][i] for j in range(NUM_FILES)]))
#     plotTracker[i] = indicator != 0


# Plot the vectors to see how closely they align
fig, ax = plt.subplots()
ind = np.arange(numsources)     # the x locations for the groups
width = 0.3                    # the width of the bars

for i in range(NUM_FILES):
    plotList = [signalMatrix[i][j] for j in range(numsources)]
    # print(plotList)
    p = ax.bar(ind+i*width, plotList , width)

ax.set_title('Change in Signals Observed in Front of Room 167')
ax.set_xticks(ind + width*(NUM_FILES-1) / 2)
ax.set_xticklabels(sourceList)
# ax.xaxis.set_tick_params(horizontalalignment='right')
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(8)
    tick.label1.set_horizontalalignment('right')
plt.xticks(rotation=20)
matplotlib.rcParams.update({'font.size': 12})

lgd = ax.legend(('Data Set 1','Data Set 2'),loc="lower right")
lgd.get_frame().set_alpha(1)
plt.ylabel("Signal Strength (dBm)")
ax.autoscale_view()

plt.show()
