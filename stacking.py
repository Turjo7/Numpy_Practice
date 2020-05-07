import numpy as np

a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)])
b = np.array([(10, 20, 30), (40, 50, 60), (70, 80, 90), (100, 110, 120)])

print(np.vstack((a,b))) #Vertical Stacking
print(np.hstack((a,b))) #Horizontal Stacking
