#Compute a matrix rank#
import numpy as np
matrix = np.array([[1,2],[3,4]])
rank = np.linalg.matrix_rank(matrix)
print(matrix)
print(rank)