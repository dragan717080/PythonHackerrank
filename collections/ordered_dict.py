d = {}

for _ in range(int(input())):
    item = input().split()
    item_name, price = " ".join(item[:-1]), int(item[-1])
    d[item_name] = d.get(item_name, 0) + price

print("\n".join([f"{k} {str(v)}" for k, v in d.items()]))
