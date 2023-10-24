 
t = int(input())
for _ in range(t):
    n = int(input())
    d = list(map(int, input().split()))


    dp = [0]*(n + 1)
    dp[-1] = 1

    for ind, length in enumerate(d):
        
        if ind - length >= 0:
            dp[ind] = dp[ind] or dp[ind - length - 1]

        if ind + length < n:
            dp[ind + length] = dp[ind + length] or dp[ind - 1] 

    # print(dp)
    if dp[-2]:
        print('YES')
    
    else:
        print('NO')