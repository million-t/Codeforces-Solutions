



n, k = map(int, input().split())
c = list(map(int, input().split()))


c.sort()
dp = [[]]*(k + 1)
dp[k] = 1


for coin in c:
    
    for ind in range(k):
    

ans = []
for ind, val in enumerate(dp):
    if val:
        ans.append(ind)

print(len(ans))
print(*ans)
