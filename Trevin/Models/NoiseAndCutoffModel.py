import numpy as np
import scipy
import math

np.random.seed(5)
np.set_printoptions(precision=2,linewidth=94)

# Initialize physical model parameters 
TX_POWER = 1000         # Transmit power of access points in milliwatts
TX_DIRECTIVITY = 1      # Directivity of transmitting antenna (one for isotropic)
RX_DIRECTIVITY = 1      # Directivity of recieving antenna (one for isotropic)
HALL_HEIGHT = 5         # Height of hall in meters
HALL_LENGTH = 40        # Length of hall in meters
NUM_ACCESS_POINTS = 10  # Number of access points visible in the hallway
NUM_LOCATIONS = 20      # Number of locations to distinguish from
FREQUENCY = 2.4e6       # Frequency of wifi in Hertz

LAMBDA = 3e8/FREQUENCY  # Wavelength of wifi in meters

# Initialize probabilistic model parameters
NOISE_SD = 5            # Standard deviation of normally distributed noise
CUTOFF_PROB = 0.1       # Probability that any given station is not visible/not responding
RAYLEIGH_SCALE = 1      # Scale parameter of Rayleigh noise distribution

# Initialize operational model parameters
NUM_TRAINING_ITERATIONS = 10000
NUM_TEST_ITERATIONS = 10000

# Generate vector for access point locations
accessPoints = np.sort(np.round(10*HALL_LENGTH*np.random.rand(NUM_ACCESS_POINTS))/10)
print("Access Point Locations: ", accessPoints, sep='')
hall = np.linspace(0,HALL_LENGTH,NUM_LOCATIONS)

# Function to generate data at a given location using the Friis equation with Rayleigh-distributed noise
def generateSignal(hallwayLocations, accessPointLocations, hallLocationNumber):
    d = np.sqrt(np.power(accessPointLocations-hallwayLocations[hallLocationNumber],2) + np.power(HALL_HEIGHT, 2))
    noise = np.random.normal(0,NOISE_SD)+1j*np.random.normal(0,NOISE_SD)
    E_field = np.sqrt(TX_POWER*TX_DIRECTIVITY*RX_DIRECTIVITY/2)*(LAMBDA/(4*np.pi*d))
    signalPower = np.power(np.abs(E_field*(1+1j)+noise),2)
    # print(signalPower)
    cutoffArray = np.random.rand(NUM_ACCESS_POINTS)
    signalPower = signalPower*((cutoffArray >= CUTOFF_PROB).astype(int)) # +0.001*(cutoffArray < CUTOFF_PROB).astype(int))
    return signalPower # 10*np.log10(signalPower)

# Initialize matrix of signal signatures for the different locations
signatureMatrix = np.zeros((NUM_LOCATIONS,NUM_ACCESS_POINTS))
countMatrix = np.zeros((NUM_LOCATIONS,NUM_ACCESS_POINTS))

# Set signal signatures for the different locations
for i in range(NUM_LOCATIONS):
    for j in range(NUM_TRAINING_ITERATIONS):
        signalReceived = generateSignal(hall, accessPoints,i)                   # get the signal strengths at the location
        nonZeroCheck = (signalReceived != 0).astype(int)                        # check if any of the signals are 0
        signatureMatrix[i] = signatureMatrix[i] + signalReceived*nonZeroCheck   # add the signal strengths, but ignore any that are 0
        countMatrix[i] = countMatrix[i] + nonZeroCheck                          # increase count for all stations that didn't have 0
    signatureMatrix[i] = signatureMatrix[i]/countMatrix[i]                      # calculate average of all strengths at that location

# Print the signature matrix, or comment it out and don't
print("Signature Matrix:\n", signatureMatrix)

# Test the program to see how accurately information matches (it should be good because it's deterministic)
numCorrect = 0
for i in range(NUM_TEST_ITERATIONS):
    trueLocation = np.random.choice(range(NUM_LOCATIONS))
    # print("trueLocation =", trueLocation)
    recievedSignal = generateSignal(hall,accessPoints,trueLocation)
    nonZeroCheck = (recievedSignal != 0).astype(int)
    matchVector = np.sum(np.power(np.tile(recievedSignal,(NUM_LOCATIONS,1)) - signatureMatrix*np.tile(nonZeroCheck,(NUM_LOCATIONS,1)),2),axis=1)
    # print("matchVector =", matchVector)
    perceivedLocation = np.argmin(matchVector)
    # print("perceivedLocation =", perceivedLocation)
    if (trueLocation == perceivedLocation):
        numCorrect = numCorrect + 1
    else:
        # sprint("Error! True Location: ", trueLocation, ", perceivedLocation: ", perceivedLocation, sep='')

# Calculate and print the number of locations correctly identified
ratioCorrect = numCorrect/NUM_TEST_ITERATIONS
print("Percent of locations identified correctly: {0:.3f}%".format(ratioCorrect*100))


