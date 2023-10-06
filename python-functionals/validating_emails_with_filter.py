import re

def fun(s):
    return bool(re.match(r'^[\w-]+@[0-9A-Za-z]+\.[A-Za-z]{1,3}$', s))

def filter_mail(emails):
    return list(filter(fun, emails))

""" n = int(input())
emails = [input() for _ in range(n)] """
n = 3
emails = ["lara@hackerrank.com", "brian-23@hackerrank.com", "britts_54@hackerrank.com", "harsh@gmail", "iota_98@hackerrank.com"]

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
