from collections import deque

d = deque()

for _ in range(int(input())):
    command = input().split()
    eval(f"d.{command[0]}()" if len(command) == 1 else f"d.{command[0]}({command[1]})")

print(" ".join([str(item) for item in d]))
