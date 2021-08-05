"""Display the Mandelbrot set

Time-stamp: <2021-08-05 16:34:42 christophe@pallier.org>

From A. K. Dewdney (1988) *The Armchair Universe: An Exploration of Computer Worlds*, W.H. Freeman and Co., New York:

"Here is the iterative process that generates the Mandelbrot set: Begin with
the algebraic expression z^2 + c, where z is a complex number that is allowed
to vary and c is a certain fixed complex number. Set z initially to be equal to
the complex number 0. The square of z is then 0 and the result of adding c to
z^2 is just c. Now substitute the result for z in the expression z^2 + c. The
new sum is c^2 + c. Again substitute for z. The next sum is (c^2 + c)^2 + c.
Continue the process, always making the output of the last step the input for
the next one. The Mandelbrot set is the set of all complex numbers c for which
the size of z^2 + c is small (e.g. less than 2.0) even after an indefinitely
large number of iterations."


For more, check out https://www.fractint.org/ and https://www.fractint.org/ftp/current/
"""

import numpy as np
import matplotlib.pyplot as plt

niterations = 100
nrow, ncol = 800, 800
xmin, xmax = -1.5, 0.5
ymin, ymax = -1.0, 1.0

xscale = np.linspace(xmin, xmax, nrow)
yscale = np.linspace(ymin, ymax, ncol)
xx, yy = np.meshgrid(xscale, yscale)

c = xx + 1j * yy
z = 0 * xx + 0 * yy

for i in range(niterations):
    z = z * z + c

val = np.abs(z)

vals = np.min(np.array([val,
                        2.0 * np.ones(shape=(nrow, ncol))]), axis=0)

plt.matshow(vals, extent=[xmin, xmax, ymin, ymax])
plt.show()
