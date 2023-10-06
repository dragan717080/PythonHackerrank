matrix = [list(map(float, input().split())) for _ in range(list(map(int, input().split()))[1])]

def transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])

    return [[matrix[j][i] for j in range(rows)] for i in range(cols)]

res = [f"{sum(row) / len(row):.1f}" for row in transpose(matrix)]
print("\n".join(res))
