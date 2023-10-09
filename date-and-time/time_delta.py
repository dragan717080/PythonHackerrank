from datetime import datetime

def time_delta(t1, t2):
    t1, t2 = map(lambda x: datetime.strptime(x, "%a %d %b %Y %H:%M:%S %z"), [t1, t2])
    return abs(int((t2-t1).total_seconds()))

for t_itr in range(int(input())):
    print(time_delta(input(), input()))
