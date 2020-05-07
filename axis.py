import numpy as np

a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)])

print(a.sum(axis=0)) # Sum of the columns
print(a.sum(axis=1)) # Sum of the rows