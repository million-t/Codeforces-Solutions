
MOD = 10**9 + 7

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())

    if a < 1:
        print(0)
        continue

    dp = [[0]*a for _ in range(a)]
    dp[0][0] = 1

    
    for row in range(1, a):
        dp[row][0] = dp[row-1][0]
        for col in range(1, row + 1):
            dp[row][col] = (dp[row-1][col] + dp[row-1][col-1]) % MOD
    
    print(2*dp[-1][b])
    