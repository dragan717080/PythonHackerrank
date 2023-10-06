n, m = map(int, input().split())

get_dots = lambda i: "-"*i*3

get_line_doormat = lambda i: '.|.' if i == 0 else f'.{"|" + "..|..|"*i}.'

n_dots = n // 2
for i in range(n // 2):
    print(get_dots(n_dots), end='')
    print(get_line_doormat(i), end='')
    print(get_dots(n_dots))
    n_dots -= 1

n_dots = (n * 3 - len('WELCOME')) // 2
print(f'{"-"*n_dots}WELCOME{"-"*n_dots}')

n_line_doormat = n // 2 - 1
for i in range(n // 2):
    print(get_dots(i + 1), end='')
    print(get_line_doormat(n_line_doormat), end='')
    print(get_dots(i + 1))
    n_line_doormat -= 1
