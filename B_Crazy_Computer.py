n, c = map(int, input().split())
nums = list(map(int, input().split()))

count = 1

for ind in range(1, n):
    if nums[ind - 1] + c < nums[ind]:
        count = 1
    
    else:
        count += 1

print(count)