
s = input()

MOD = 1_000_000_007


letters = set(s)
if 'm' in letters or 'w' in letters:
    print(0)

else:
    ans = 1
    n = len(s)
    if n < 2:
        print(ans) 
        exit()

    dp = [0]*n

    dp[0] = 1
    dp[1] = 2
    for ind in range(2, n):
        dp[ind] = (dp[ind - 1] + dp[ind - 2])%MOD

    left = right = 0
    while right < n:
        while right < n - 1 and (s[right + 1] == s[left] == 'n' or s[right + 1] == s[left] == 'u'):
            right += 1
        
        ans = (ans*dp[right - left])%MOD
        right += 1
        left = right
    
    print(ans)