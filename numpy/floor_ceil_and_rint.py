import numpy as np

np.set_printoptions(legacy='1.13')
a = list(map(float, input().split()))
print(f"{np.floor(a)}\n{np.ceil(a)}\n{np.rint(a)}")
