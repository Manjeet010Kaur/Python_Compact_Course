"""Consider two random array A and B, check 
if they are equal"""
import numpy as np
a = np.random.random(5)
b = np.random.random(5)
print(a,b)
print(np.array_equal(a,b))