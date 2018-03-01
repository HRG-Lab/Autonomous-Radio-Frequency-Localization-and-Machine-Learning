import numpy as np
import scipy
import math
import matplotlib.pyplot as plt

NUM_TRIALS = 1000000
RAYLEIGH_SCALE = 1 # np.sqrt(2/np.pi)
STANDARD_DEVIATION = 1

np.random.seed(4)

bins = np.arange(0,5,0.01)
rayleighProbabilities = np.zeros(len(bins))
normalProbabilities = np.zeros(len(bins))
rayleighValues = np.zeros(NUM_TRIALS)
normalValues = np.zeros(NUM_TRIALS)
# yValues = np.zeros(NUM_TRIALS)

for i in range(NUM_TRIALS):
    rayleighValues[i] = np.random.rayleigh(RAYLEIGH_SCALE)
    normalValues[i] = np.sqrt(np.power(np.random.normal(0,STANDARD_DEVIATION),2) + np.power(np.random.normal(0,STANDARD_DEVIATION),2))
    # yValues[i] = np.random.normal(0,STANDARD_DEVIATION)

for b in range(len(bins)-1):
    rayleighProbabilities[b] = sum(1 for i in rayleighValues if (i >= bins[b] and i < bins[b+1]))/NUM_TRIALS
    normalProbabilities[b] = sum(1 for i in normalValues if (i >= bins[b] and i < bins[b+1]))/NUM_TRIALS

print(rayleighProbabilities)
plt.plot(bins,rayleighProbabilities)
plt.plot(bins,normalProbabilities)
plt.show()