from math import gcd

n = int(input())
nums = list(map(int, input().split()))

nums.reverse()


last_gcd = nums[0]
ans = 0


for ind in range(1, n):
    new_gcd = gcd(last_gcd, nums[ind])
    ans = gcd(ans, nums[ind]*last_gcd//new_gcd)
    last_gcd = new_gcd


print(ans)