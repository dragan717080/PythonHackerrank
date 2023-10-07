import numpy as np

n = int(input())
a, b = map(lambda x: np.array([input().split() for _ in range(x)], int), [n, n])

print(np.dot(a, b))
