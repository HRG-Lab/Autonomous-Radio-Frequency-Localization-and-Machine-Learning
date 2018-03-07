import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# from matplotlib import rc
# rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})

np.random.seed(11)
np.set_printoptions(precision=1,linewidth=94,threshold=1000)

# Initialize physical model parameters 
TX_POWER = 1000         # Transmit power of access points in milliwatts
TX_DIRECTIVITY = 1      # Directivity of transmitting antenna (one for isotropic)
RX_DIRECTIVITY = 1      # Directivity of recieving antenna (one for isotropic)
HALL_HEIGHT = 5         # Height of hall in meters
HALL_LENGTH = 40        # Length of hall in meters
NUM_ACCESS_POINTS = 5   # Number of access points visible in the hallway
NUM_LOCATIONS = 20      # Number of locations to distinguish from
FREQUENCY = 2.4e6       # Frequency of wifi in Hertz

LAMBDA = 3e8/FREQUENCY  # Wavelength of wifi in meters

# Initialize probabilistic model parameters
POWER_NOISE_STD_DEV = 500          # Standard deviation of normally distributed noise

# Initialize operational model parameters
PLOT_STEP = 0.01
PLOT_ALL = True
TEST_LOCATION = 24.1 # np.random.uniform(0,HALL_LENGTH)

# Generate vector for access point locations
accessPoints = np.sort(np.round(10*HALL_LENGTH*np.random.rand(NUM_ACCESS_POINTS))/10)
print("Access Point Locations: ", accessPoints,sep='')
print("Standard Deviation of Noise: ", POWER_NOISE_STD_DEV, " milliwatts",sep='')
# hall = np.linspace(0,HALL_LENGTH,NUM_LOCATIONS)

# Function to generate data at a given location using the Friis equation with Rayleigh-distributed noise
def generateSignal(location, accessPointLocations):
    d = np.sqrt(np.power(accessPointLocations-location,2) + np.power(HALL_HEIGHT, 2))
    noise = np.random.normal(0,POWER_NOISE_STD_DEV)
    # E_field = np.sqrt(TX_POWER*TX_DIRECTIVITY*RX_DIRECTIVITY/2)*(LAMBDA/(4*np.pi*d))
    signalPowerVector = TX_POWER*TX_DIRECTIVITY*RX_DIRECTIVITY*np.power(LAMBDA/(4*np.pi*d),2) + noise
    # print(signalPowerVector)
    # randVect = np.random.rand(NUM_ACCESS_POINTS)
    # print(randVect)
    # print(signalPowerVector*(1*(np.random.rand(NUM_ACCESS_POINTS) <= 0.6)))
    for i in range(NUM_ACCESS_POINTS):
        if (np.random.rand() <= dropOutProbability(d[i])):
            signalPowerVector[i] = 0
    print("Signal received: ", signalPowerVector, sep='')
    return abs(signalPowerVector) # 10*np.log10(signalPower)


def dropOutProbability(distance):
    prob = np.power(distance/15,8)
    if prob > 1:
        prob = 1
    return prob

# Function to get the probabilty of seeing a certain signal strength at a location
def signalProbability(receivedSignal, location, accessPointLocations, accessPointLocationNumber):
    d = np.sqrt(np.power(accessPointLocations[accessPointLocationNumber]-location,2) + np.power(HALL_HEIGHT, 2))
    if (receivedSignal != 0):
        signalPower = TX_POWER*TX_DIRECTIVITY*RX_DIRECTIVITY*np.power(LAMBDA/(4*np.pi*d),2)
        powerDifference = -abs(receivedSignal - signalPower)
        prob = norm.pdf(powerDifference,scale=POWER_NOISE_STD_DEV)
        prob = prob*(1-dropOutProbability(d))
    else:
        prob = dropOutProbability(d)
    return prob


# Function to generate probability distribution given data from sensor
def locationProbability(receivedSignalVector, accessPointLocations, plotDistribution=False, plotAll=False):
    hallwayPoints = np.arange(0, HALL_LENGTH, PLOT_STEP)
    probabilityMatrix = np.zeros((len(hallwayPoints),NUM_ACCESS_POINTS))
    for i in range(len(hallwayPoints)):
        for j in range(NUM_ACCESS_POINTS):
            probabilityMatrix[i][j] = signalProbability(receivedSignalVector[j],hallwayPoints[i],accessPointLocations,j)
    probabilityDistribution = np.prod(probabilityMatrix,axis=1)
    probabilityDistribution = probabilityDistribution/(PLOT_STEP*np.sum(probabilityDistribution))
    if (plotDistribution):
        plt.plot(hallwayPoints,probabilityDistribution,label='Probability',color='red')
        plt.axvline(x=TEST_LOCATION,color='k',linestyle='--',label='True Location')
        if (plotAll):
            for i in range(NUM_ACCESS_POINTS):
                line, = plt.plot(hallwayPoints,probabilityMatrix[:,i]/(PLOT_STEP*np.sum(probabilityMatrix[:,i])),label=('Access Point ' + str(i)))
                plt.plot(accessPointLocations[i], max(probabilityDistribution), '.', color=line.get_color())
        else:
            plt.plot(accessPoints,np.ones(NUM_ACCESS_POINTS)*max(distribution),'.',label='Access Points')
        plt.title('Probability Distribution Across the Hallway with Power Noise StdDev = ' + str(POWER_NOISE_STD_DEV) + ' mW')
        plt.xlabel('Hallway Position (m)')
        plt.ylabel('Probability Density')
        plt.legend(loc='lower left', shadow=True)
    return probabilityDistribution



print("Test Location: ", TEST_LOCATION, sep='')
distribution = locationProbability(generateSignal(TEST_LOCATION,accessPoints),accessPoints,plotDistribution=True,plotAll=PLOT_ALL)

plt.show()
