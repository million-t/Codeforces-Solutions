from math import log
x = int(input())


ans = 0
while x:
    ans += 1
    x = x - 2**int(log(x, 2))

print(ans)