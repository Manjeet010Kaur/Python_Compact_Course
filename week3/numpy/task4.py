"""Multiply a 5x3 matrix by a 3x2 matrix (real 
matrix product) """
import numpy as np
a = np.random.random((5,3))
print(a)
b = np.random.random((3,2))
print(b)
c = np.dot(a,b)
print(c)