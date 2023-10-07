import numpy as np

matrix = np.array([list(map(int, input().split())) for _ in range(list(map(int, input().split()))[0])])
print(np.prod(np.sum(matrix, axis=0)))
