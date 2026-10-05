"""Create a structured array representing a 
position (x,y) and a color (r,g,b)"""
import numpy as np
dtype = [('x', 'f4'),
         ('y', 'f4'),
         ('r', 'i4'),
         ('g', 'i4'),
         ('b', 'i4')]
data = np.array([(10.4, 38.3, 255, 0, 100)], dtype = dtype)
print("Structured array :", data)
print("x ", data['x'])
print("y", data['y'])
print("red", data['r'])
print("green ", data['g'])
print("blue ", data['b'])