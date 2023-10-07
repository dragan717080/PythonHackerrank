all_elements = [[input(), float(input())] for _ in range(int(input()))]

second_lowest_grade = list(set(sorted(list(zip(*all_elements))[1])))[1]
print("\n".join(sorted([item[0] for item in list(filter(lambda student: student[1] == second_lowest_grade, all_elements))])))
