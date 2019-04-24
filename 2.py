import numpy as np
import math

e = np.array([0, 1.8, 10])
c = np.array([0, 3, 0])
up = np.array([0, 1, 0])

cminusE = c-e
f = cminusE / math.sqrt(cminusE[0] ** 2 + cminusE[1] ** 2 + cminusE[2] ** 2)
d = cminusE.normalised()
print(f)
print(d)