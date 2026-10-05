""" Create a vector with values ranging from 
10 to 49.  Reverse a vector (first element 
becomes last) """

import numpy as np
vector = np.arange(10, 50)
print("original vector", vector)
print("reversed vector", vector[:: -1])