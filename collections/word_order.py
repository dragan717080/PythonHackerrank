from collections import Counter

words = [input() for _ in range(int(input()))]

print(f"{len(set(words))}\n{' '.join([str(v) for v in Counter(words).values()])}")
