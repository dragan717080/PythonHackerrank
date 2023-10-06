cube = lambda x: x**3
def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    arr = [0, 1]
    for _ in range(2, n):
        arr.append(sum(arr[-2:]))
    return arr

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
