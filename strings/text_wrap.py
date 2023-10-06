import math

s = input()
n = int(input())

def wrap(s, n):
    res = [s[i*n : i*n +n] for i in range(math.ceil(len(s) / n))]
    return "\n".join(res)

wrap(s, n)
