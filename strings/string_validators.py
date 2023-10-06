import re

#s = input()
s = "qA2"

patterns = ['[0-9a-zA-Z]', '[a-zA-Z]', '\\d', '[a-z]', '[A-Z]']
print("\n".join([str(bool(re.search(pattern, s))) for pattern in patterns]))
