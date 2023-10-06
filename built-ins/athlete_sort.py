matrix = [list(map(int, input().split())) for _ in range(list(map(int, input().split()))[0])]
k = int(input())
matrix = sorted(matrix, key = lambda x: x[k])
print("\n".join([" ".join([str(d) for d in row]) for row in matrix]))
