import datetime

m, d, y = map(int ,input().split())
print(datetime.datetime(y, m, d).strftime("%A").upper())
