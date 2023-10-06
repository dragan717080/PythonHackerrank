import re

s = input()

match = lambda pattern, c: bool(re.match(f'{pattern}', c))
res = "".join(sorted([c for c in s], key = lambda c: (match('\d', c), int(c) % 2 == 0 if match('\d', c) else 0, match('[A-Z]', c), c)))
print(res)
