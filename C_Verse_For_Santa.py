from collections import defaultdict


t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    
    dp = [[0]*2 for _ in range(n)]
    jumps = defaultdict(int)

    dp[0][0] = a[0]
    
    count = [[0]*2 for _ in range(n)]
    count[0][0] = 1
    ans = 0

    for ind in range(1, n):
        time = a[ind] 

        if dp[ind - 1][0] + time <= s:
            dp[ind][0] = dp[ind - 1][0] + time
            count[ind][0] = count[ind - 1][0]
            ans = n - count[ind][0]
        
        if dp[ind - 1][1] + time < dp[ind][0]:
            dp[ind][0] = dp[ind - 1][1] + time
            count[ind][0] = count[ind - 1][1]
            ans = n - count[ind][0]

        dp[ind][1] = dp[ind - 1][0]
        count[ind][1] = count[ind - 1][0] + 1 

    print(count)
    print(dp)
    print(ans)
