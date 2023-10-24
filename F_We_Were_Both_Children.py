from math import gcd
from collections import defaultdict, Counter


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # a.sort()
    seen = Counter(a)
    temp = defaultdict(int)
    for ind in range(n + 1):

        for i in range(1, int(ind**0.5) + 1):
            mod, div = ind%i, ind//i
            if mod == 0:
                if i in seen:
                    temp[ind] += seen[i]
                
                if div != i and div in seen:
                    temp[ind] += seen[div]

    ans = 0
    # print(temp)
    
    for mult, count in temp.items():
        ans = max(ans, count)

    
    print(ans)



        