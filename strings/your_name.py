def mutate_string(s, i, c):
    return "".join(map(lambda item: item[1] if item[0] != i else c, enumerate([c for c in s])))

s = input()
i, c = list(map(lambda item: int(item[1]) if item[0] == 0 else item[1], enumerate(input().split())))
print(mutate_string(s, i, c))
