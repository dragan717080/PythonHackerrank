import numpy as np

def arrays(arr):
    arr.reverse()
    return np.array(arr, dtype=int)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
