from collections import defaultdict

from collections import defaultdict
ls = [1,10,2,90,3,44,32,67,78,45,50,55,16]
d =defaultdict(list)
for i in ls:
    d[i//10].append(i)
for k,v in d.items():
    print(f"{k}:{v}")