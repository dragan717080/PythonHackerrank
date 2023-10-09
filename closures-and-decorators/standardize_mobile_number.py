def wrapper(f):
    def fun(l):
        l = ['+91 '+i[-10:-5]+' '+i[-5:] for i in l]
        f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

sort_phone([input() for _ in range(int(input()))])
