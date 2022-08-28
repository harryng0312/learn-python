import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S4')

print(f"NP Array: {arr} ID: {id(arr)}")
print(f"NP Array type:{arr.dtype}")
print(f"Py Array:{arr.astype(dtype=int)} size: {id(arr.astype(int))}")