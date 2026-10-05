"""Create a 5x5 array with random values. 
and find the minimum and maximum 
values """

import numpy as np
matrix = np.random.random((5, 5))
print(matrix)
print(matrix.min())
print(matrix.max())