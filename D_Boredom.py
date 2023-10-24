from collections import Counter

n = int(input())
a = list(map(int, input().split()))


count = Counter(a)

dp = []

for num, freq in count.items():
    dp.append((num, freq))

dp.sort()


size = len(dp)
if size == 1:
    print(dp[0][1]*dp[0][0])
    exit()


memo = [0]*size
memo[0] = dp[0][1]*dp[0][0]

if dp[0][0] == dp[1][0] - 1:

    memo[1] = max(dp[0][1]*dp[0][0], dp[1][1]*dp[1][0])

else:
    memo[1] = dp[0][1]*dp[0][0] + dp[1][1]*dp[1][0]


for ind in range(2, size):
    if dp[ind][0] == dp[ind - 1][0] + 1:
        memo[ind] = max(memo[ind - 1], memo[ind - 2] + dp[ind][1]*dp[ind][0])
    else:
        
        memo[ind] = dp[ind][1]*dp[ind][0] + memo[ind - 1]


  
print(max(memo[-1], memo[-2]))



