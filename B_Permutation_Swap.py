from math import gcd
t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    k = 0
    for ind, num in enumerate(nums):
        k = gcd(k, abs(ind + 1 - num))


    print(k)