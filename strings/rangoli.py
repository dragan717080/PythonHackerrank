def get_letters_for_line(lines, n):
    distance_from_max_line = (lines - n) / 2
    min_letter = chr(ord('a') + int(distance_from_max_line))
    max_letter = chr(ord('a') + lines // 2)
    letters = [*[chr(ord(max_letter) - i) for i in range(n // 2)], *[chr(ord(min_letter) + i) for i in range(n // 2 + 1)]]
    return "-".join(letters)

def print_rangoli(n):
    lines = n * 2 - 1
    n_dots = [*[i*2 for i in range(lines // 2, 0, -1)], *[i*2 for i in range(lines // 2 + 1)]]
    n_letters = [*[i*2 + 1 for i in range(lines // 2 + 1)], *[i*2 - 1 for i in range(lines // 2, 0, -1)]]
    for i in range(lines):
        print("-"*n_dots[i], end="")
        print(get_letters_for_line(lines, n_letters[i]), end='')
        print("-"*n_dots[i])

n = int(input())

print_rangoli(n)
