import math

def get_unique_chars(s):
    return "".join(list({c:1 for c in [c for c in s]}.keys()))

def merge_the_tools(s, k):
    res = [get_unique_chars(s[i*k:i*k + k]) for i in range(math.ceil(len(s) / k))]
    print("\n".join(res))

string, k = input(), int(input())
merge_the_tools(string, k)
