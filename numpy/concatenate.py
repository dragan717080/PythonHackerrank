import numpy as np

n, m, _ = map(int, input().split())
a, b = map(lambda x: np.array([input().split() for _ in range(x)], int), [n, m])

print(np.concatenate((a, b), axis=0))
