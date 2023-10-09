import re

print(*list("Valid" if bool(re.match(r"^(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})(?!.*(.).*\1)[A-Za-z0-9]{10}$", input())) else "Invalid" for _ in range(int(input()))), sep="\n")
