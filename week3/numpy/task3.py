#Normalize a 5x5 random matrix#
import numpy as np
matrix = np.random.random((5,5))
print("original matrix : ", matrix)
norm_matrix = (matrix -matrix.min()) /  (matrix.max() - matrix.min())
print("Normalized matrix : ", norm_matrix)