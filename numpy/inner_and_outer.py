import numpy as np

a = np.array(list(map(int, input().split())), int)
b = np.array(list(map(int, input().split())), int)

print(f"{np.inner(a, b)}\n{np.outer(a, b)}")
