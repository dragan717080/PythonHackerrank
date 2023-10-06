def is_leap(year):
    return True if not year % 400 else False if not year % 100 else True if not year % 4 else False

print(is_leap(int(input())))
