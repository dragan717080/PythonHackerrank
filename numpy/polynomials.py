from functools import reduce

coefs = list(map(float, input().split()))
x = int(input())

print(reduce(lambda sum, coef: sum*x + coef, coefs, 0))
