import numpy as ns
from numpy.random import rand, randn

import matplotlib.pyplot as plt


# Mike Cohen FTFAMO p.28
Yu = rand(1000)
Yn = randn(1000)

plt.plot(Yn, color='black')
plt.plot(Yu, color='red')
plt.title('Random noise over time')
plt.legend(['Normal','Uniform'])
plt.show()

wn = randn(1000)
wnX = fft(wn)
