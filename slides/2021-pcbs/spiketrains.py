import numpy as np
import matplotlib.pyplot as plt

spiketrain = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0])

spiketimes = spiketrain.nonzero()
plt.vlines(spiketimes, 0, 1)
plt.xlim([0, len(spiketrain])
plt.show()
