from math import gcd

n = int(input())
a = list(map(int, input().split()))




run_gcd = 0
left = 0

for right, num in enumerate(a):
    run_gcd = gcd(run_gcd, num)

    while left <= right and gcd(num, a[left]) > 1:
        left += 1  
