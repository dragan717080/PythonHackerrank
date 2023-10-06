_ = int(input())
a = set(list(map(int, input().split(' '))))
_ = int(input())
b = set(list(map(int, input().split(' '))))

print(len(a.symmetric_difference(b)))
