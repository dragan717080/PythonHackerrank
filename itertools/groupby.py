from itertools import groupby 

print(*[(len(list(grp)),int(key)) for key,grp in groupby(str(input()))], sep=' ')
