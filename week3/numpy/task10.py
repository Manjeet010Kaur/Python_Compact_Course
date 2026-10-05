"""Consider a random vector with shape 
(100,2) representing coordinates, find 
point by point distances"""
import numpy as np
points = np.random.random((100,2))
print(points)
x = points[:,0]
y = points[:,1]
x = np.atleast_2d(x)
y = np.atleast_2d(y)
distances = np.sqrt((x-x.T)**2 + (y-y.T)**2)
print("cordinates : ")
print(points)
print("point by point distances : ")
print(distances)