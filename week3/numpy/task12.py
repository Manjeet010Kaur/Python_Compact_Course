#How to I sort an array by the nth column?#
import numpy as np
matrix = np.array([[3,8,2],[1,5,9],[4,2,6]])
print("original matrix", matrix)
sorted_matrix = matrix[matrix[:,1].argsort()]
print("sorted matrix", sorted_matrix)