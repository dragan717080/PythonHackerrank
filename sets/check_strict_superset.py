import sys

a = set(map(int, input().split()))
n = int(input())
all_sets = [set(list(map(int, input().split()))) for _ in range(n)]

for test_set in all_sets:
    if not a.issuperset(test_set):
        print(False)
        sys.exit(0)
print(True)
