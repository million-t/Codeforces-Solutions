from collections import defaultdict


n = int(input())
a = list(map(int, input().split()))


dp = defaultdict(int)

for num in a:
    dp[num] = max(dp[num], dp[num - 1] + 1)


cur_end = a[0]
cur_length = 1

for end, length in dp.items():
    if length >= cur_length:
        cur_end = end
        cur_length = length  

ans = []


for ind in range(n - 1, -1, -1):

    num = a[ind]
    if num == cur_end:
        ans.append(ind + 1)
        cur_end -= 1

print(len(ans))
print(*ans[::-1])
    

