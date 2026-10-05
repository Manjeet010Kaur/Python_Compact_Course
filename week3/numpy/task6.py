""" Extract the integer part of a random array 
using 5 different methods """
import numpy as np
random_array = np.random.random((5))*10
print(random_array)
m1 = np.floor(random_array)
print(m1)
m2 = random_array.astype(int)
print(m2)
m3 = np.trunc(random_array)
print(m3)
m4 = random_array//1
print(m4)
m5 = np.fix(random_array)
print(m5)