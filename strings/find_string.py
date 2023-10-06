import re

def count_substring(s1, s2):
    return len(list(re.finditer(f'(?=({s2}))', s1)))

string, sub_string = input(), input()
count_substring(string, sub_string)
