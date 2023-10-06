_ = int(input())
a = set(list(map(int, input().split(' '))))
n = int(input())

for _ in range(n):
    [command, elements_to_update], elements = map(lambda item: int(item[1]) if item[0] != 0 else item[1], enumerate(input().split())), set(list(map(int, input().split())))
    eval(f"a.{command}({elements})")
print(sum(a))
