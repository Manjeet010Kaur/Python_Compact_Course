"""Subtract the mean of each row of a matrix"""
import numpy as np
matrix = np.array([[1,2,3],[4,5,6]])
row_mean = matrix.mean(axis = 1, keepdims = True)
result = matrix -row_mean
print("original matrix ", matrix)
print ("mean of each row ", row_mean)
print(result)
