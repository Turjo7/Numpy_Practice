import numpy as np 

a = np.array([(1,2,3),(4,5,6),(7,8,9),(10,11,12)])
print(a)
a = a.reshape(3,4) # Columns-> Rows, Rows -> Columns
print(a)