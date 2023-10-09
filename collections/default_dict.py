n, m = map(int, input().split())

d = {}

d['a'] = [input() for _ in range(n)]
d['b'] = [input() for _ in range(m)]

indices = list(map(lambda x: x if len(x) else [-1], [[i + 1 for i, v in enumerate(d['a']) if v == word] for word in d['b']]))
print("\n".join([" ".join(map(str, sublist)) for sublist in indices]))
