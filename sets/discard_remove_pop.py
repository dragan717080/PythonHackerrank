_ = int(input())
a = set(list(map(int, input().split())))
n = int(input())

for _ in range(n):
    command = input()
    if command[0]=='p':
        try:
            a.discard(list(a)[0])
        except IndexError:
            pass
    else:
        a.discard(int(command[-1]))

print(sum(a))
