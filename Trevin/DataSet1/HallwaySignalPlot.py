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

# Boolean to control whether the strongest signals are included in the plot
plotStrongest = False

# Pull in the data from the nth csv file and put addresses into addressList, signal strengths
# into the nth column of signalStrengths, and number of frames from that address into addressCount
for tile in range(NUM_POSITIONS):
    filename = 'Tile ' + str(tile) + '.csv'
    print("Parsing file '", filename,"'",sep='')
    with open(filename,mode='r') as csvData:
        hallData = csv.reader(csvData, dialect='excel')
        rowNum = 0
        for row in hallData:
            if rowNum==0:
                header = row
            else:
                address = row[2]
                signalStrength = row[7]
                if signalStrength.endswith(' dBm'):
                    signalStrength = int(signalStrength[:-4])
                elif signalStrength=='':
                    rowNum += 1
                    break
                try:
                    position = addressList.index(address)
                    signalStrengths[tile][position] += signalStrength
                    addressCount[tile][position] += 1
                except ValueError:
                    addressList.append(address)
                    signalStrengths[tile].append(signalStrength)
                    addressCount[tile].append(1)
            rowNum += 1
        # Divide the signal strengths by number observed to get the average strength for that address
        signalStrengths[tile] = [x/y if y!=0 else 0 for x,y in zip(signalStrengths[tile],addressCount[tile])]
    # Initialize the next position with a bunch of zeros
    if tile != NUM_POSITIONS-1:
        signalStrengths[tile+1] = [0 for i in signalStrengths[tile]]
        addressCount[tile+1] = [0 for i in addressCount[tile]]

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

# Plot all of them in the first subplot
# plt.subplot(2,1,1)

for i in range(len(addressList)):
    if (max([addressCount[j][i] for j in range(NUM_POSITIONS)]) > 600):
        plt.plot(range(NUM_POSITIONS),[signalStrengths[j][i] for j in range(NUM_POSITIONS)],label=addressList[i])


# plt.ylim(ymax=0.0000001) # Adjust the maximum value of the y axis
plt.title("RSSI Signal Powers Across Hallway in dBm")
plt.ylabel("Signal Power (dBm)")
plt.xlabel("Hallway Position (tile number)")
plt.legend(loc='lower left')

# Plot the ones that had smaller signal strengths in the second subplot
# plt.subplot(2,1,2)

# for i in range(len(addressList)):
#     if (max([addressCount[j][i] for j in range(NUM_POSITIONS)]) > 600) and (max([signalStrengths[j][i] for j in range(NUM_POSITIONS)]) < 1e-6):
#         plt.plot(range(NUM_POSITIONS),[signalStrengths[j][i] for j in range(NUM_POSITIONS)],label=addressList[i])


# plt.title("Signal Powers Across Hallway")
# plt.ylabel("Signal Power (mW)")
# plt.xlabel("Hallway Position (tile number)")
# # plt.legend(loc='center left')

# plt.tight_layout()
plt.show()
