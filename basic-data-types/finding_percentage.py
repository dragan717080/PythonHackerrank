all_elements = [[word[1] if word[0] == 0 else float(word[1]) for word in enumerate(input().split())] for _ in range(int(input()))]

ind = list(zip(*all_elements))[0].index(input())
grades = all_elements[ind][1:]
print(f"{sum(grades) / len(grades):.2f}")
