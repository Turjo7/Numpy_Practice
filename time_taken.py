import numpy as np
import time
import sys

size = 100000000

L1 = range(size)
L2 = range(size)

A1 = np.arange(size)
A2 = np.arange(size)

start = time.time()

result_1 = [x + y for x, y in zip(L1,L2)]
print((time.time()-start)*1000)

start = time.time()

result_2 = A1+A2
print((time.time()-start)*1000)