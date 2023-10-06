from collections import Counter

_ = input()
for k,v in Counter(input().split()).items():
    if v == 1:
        print(k)
        break
