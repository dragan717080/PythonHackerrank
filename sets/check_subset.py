for _ in range(int(input())):
    _ = int(input())
    a = set(list(map(int, input().split())))
    _ = int(input())
    b = set(list(map(int, input().split())))
    print(a.issubset(b))
