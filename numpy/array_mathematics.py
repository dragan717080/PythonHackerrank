import numpy as np

n, m = map(int, input().split())
a, b = map(lambda x: np.array([input().split() for _ in range(x)], int), [n, n])

print(f"{a + b}\n{a - b}\n{a * b}\n{a // b}\n{a % b}\n{a**b}")
