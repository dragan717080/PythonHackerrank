from itertools import product
from functools import reduce

n, k = map(int, input().split())
#n, k = 3, 1000
a = [[2, 5, 4], [3, 7, 8, 9], [5, 5, 7, 8, 9, 10]]
a = [list(map(int, input().split()[1:])) for _ in range(n)]
print(a)