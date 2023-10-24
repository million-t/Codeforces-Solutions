from math import sqrt

import sys

inp = list(sys.stdin)
t = int(inp[0])
i = 1

for _ in range(t):
    n = int(inp[i])
    i += 1

    left = 1
    prev = 1
    ans = 1 

    for num in range(2, int(sqrt(n)) + 2):
        if n%num == 0:
            if prev + 1 == num:
                ans = max(ans, num - left + 1)

            else:
                left = num

            prev = num
            

        

        
    print(ans)


