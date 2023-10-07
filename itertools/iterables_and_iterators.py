from itertools import permutations

n = int(input())
a = input().split()
k = int(input())

count = total = 0
for perm in permutations(a, k):
    total += 1
    if 'a' in perm:
        count += 1
        
print(count / total)
