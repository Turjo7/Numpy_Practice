import numpy as np

a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)])
print(a[0, 2])  # From the first row, picks the third element
print(a[0:, 2])  # From the first to last clomuns, picks the third element
print(a[0:3, 2])  # From the first to third columns, picks the third element

