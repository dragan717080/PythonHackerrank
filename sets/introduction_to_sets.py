def average(array):
    a = set(array)
    return round(sum(a) / len(a), 3)

n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)
