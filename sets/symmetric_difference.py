_ = int(input())
a = set(list(map(int, input().split(' '))))
_ = int(input())
b = set(list(map(int, input().split(' '))))

print("\n".join([str(d) for d in sorted(a.symmetric_difference(b))]))
