
n = int(input())
nums = list(map(int, input().split()))

dec = [1]*n
inc = [1]*n

for ind in range(1, n):
    if nums[ind] > nums[ind - 1]:
        inc[ind] += inc[ind - 1]

for ind in range(n - 2, -1, -1):
    if nums[ind] < nums[ind + 1]:
        dec[ind] += dec[ind + 1]

ans = 0
for ind in range(n):
    if ind > 2 and nums[ind - 2] < nums[ind] and (not nums[ind - 2] < nums[ind - 1] < nums[ind]):
        ans = max(ans, inc[ind - 2] + dec[ind])
    
    else:
        ans = max(ans, inc[ind])

print(ans)