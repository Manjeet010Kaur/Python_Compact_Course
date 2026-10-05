"""Consider a 16x16 array, how to get the 
block-sum (block size is 4x4)"""
import numpy as np
array = np.arange(1,257).reshape(16,16)
print("originl matrix", array)
blocks = array.reshape (4,4,4,4)
block_Sum = blocks.sum(axis = (1,3))
print(block_Sum)