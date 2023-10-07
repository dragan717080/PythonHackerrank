import numpy as np

matrix = np.array([list(map(int, input().split())) for _ in range(list(map(int, input().split()))[0])])
print(np.max(np.min(matrix, axis=1)))
