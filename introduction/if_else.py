n = int(input())
print("Weird" if n % 2 else "Not Weird" if n in range(2, 6) else "Weird" if n in range(6, 21) else "Not Weird")
