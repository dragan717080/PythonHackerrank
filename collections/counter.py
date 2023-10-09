from collections import Counter

_ = int(input())
availables = dict(Counter(list(map(int, input().split()))))

total = 0

for _ in range(int(input())):
    num, price = map(int, (input().split()))
    if num not in availables:
        continue
    if availables[num]:
        availables[num] -= 1
        total += price

print(total)
