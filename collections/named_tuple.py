n = int(input())
ind = input().split().index("MARKS")
marks = list(map(int, list(zip(*[input().split() for _ in range(n)]))[ind]))
print(f"{sum(marks) / len(marks):.2f}")
