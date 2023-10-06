for _ in range(int(input())):
    print_error =  lambda e: print("Error Code:", e)
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError as e:
        print_error(e)
    except ValueError as e:
        print_error(e)
