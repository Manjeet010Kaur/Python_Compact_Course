"""Consider a generator function that 
generates 10 integers and use it to build an 
array"""
import numpy as np
def generate_num():
    for i in range(1,11):
        yield i
numbers = generate_num()
array = np.array(list(numbers))
print(array)