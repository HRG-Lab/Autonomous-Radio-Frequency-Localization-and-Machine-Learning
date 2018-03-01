import numpy as np
import scipy
import math

np.random.seed(3)
np.set_printoptions(precision=3,linewidth=94)

# Initialize physical model parameters 
TX_POWER_DBM = 30       # Transmit power of access points in dBm
TX_GAIN_DBM = 0         # Gain of transmitting antenna in dBm (zero for isotropic)
RX_GAIN_DBM = 0         # Gain of recieving antenna in dBm (zero for isotropic)
HALL_HEIGHT = 5         # Height of hall in meters
HALL_LENGTH = 40        # Length of hall in meters
NUM_ACCESS_POINTS = 10  # Number of access points visible in the hallway
NUM_LOCATIONS = 20      # Number of locations to distinguish from
FREQUENCY = 2.4e6       # Frequency of wifi in Hertz

LAMBDA = 3e8/FREQUENCY  # Wavelength of wifi in meters

# Initialize operational model parameters
NUM_TEST_ITERATIONS = 1000

# Generate vector for access point locations
accessPoints = np.sort(np.round(10*HALL_LENGTH*np.random.rand(NUM_ACCESS_POINTS))/10)
hall = np.linspace(0,HALL_LENGTH,NUM_LOCATIONS)

# Function to generate data at a given location using the Friis equation (deterministic)
def generateSignal(hallwayLocations, accessPointLocations, hallLocationNumber):
    d = np.sqrt(np.power(accessPointLocations-hallwayLocations[hallLocationNumber],2) + np.power(HALL_HEIGHT, 2))
    return (TX_POWER_DBM + 20*np.log10(LAMBDA/(4*np.pi*d)))

# Initialize matrix of signal signatures for the different locations
signatureMatrix = np.zeros((NUM_LOCATIONS,NUM_ACCESS_POINTS))

# Set signal signatures for the different locations
for i in range(NUM_LOCATIONS):
    signatureMatrix[i] = generateSignal(hall, accessPoints,i)

# Print the signature matrix, or comment it out and don't
print("Signature Matrix:\n", signatureMatrix)

# Test the program to see how accurately information matches (it should be good because it's deterministic)
numCorrect = 0
for i in range(NUM_TEST_ITERATIONS):
    trueLocation = np.random.choice(range(NUM_LOCATIONS))
    recievedSignal = generateSignal(hall,accessPoints,trueLocation)
    matchVector = np.sum((np.tile(recievedSignal,(NUM_LOCATIONS,1)) == signatureMatrix).astype(int),axis=1)
    percievedLocation = np.nonzero(matchVector == NUM_ACCESS_POINTS)
    if (trueLocation == percievedLocation):
        numCorrect = numCorrect + 1
    else:
        print("Error! True Location:", trueLocation, ", PercievedLocation:", percievedLocation)

# Calculate and print the number of locations correctly identified
ratioCorrect = numCorrect/NUM_TEST_ITERATIONS
print("Percent of locations identified correctly: {0:.3f}%".format(ratioCorrect*100))


