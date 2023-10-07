a = []

for _ in range(int(input())):
    command = input().split()
    if len(command) == 1:
        if command[0] == "print":
            print(a)
        else:
            eval(f"a.{command[0]}()")
    elif len(command) == 2:
        eval(f"a.{command[0]}({command[1]})")
    else:
        eval(f"a.{command[0]}({command[1]}, {command[2]})")
