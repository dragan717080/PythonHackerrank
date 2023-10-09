import re

pattern = r'(?<=[^aeiou\s\d\W_])([aeiou]{2,})(?=[^aeiou\s\d\W_])'
a = re.findall(pattern, input(), re.IGNORECASE)
print(*a, sep='\n') if a else print(-1)
