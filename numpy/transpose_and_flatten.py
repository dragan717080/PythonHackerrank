import numpy as np

matrix = np.array([list(map(int, input().split())) for _ in range(list(map(int, input().split()))[0])])

print(np.transpose(matrix))
print(matrix.flatten())
