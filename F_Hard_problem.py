

n = int(input())
c = list(map(int, input().split()))
strings = []
rev_str = []
for _ in range(n):
    string = input()
    strings.append(string)
    rev_str.append(string[::-1])


as_is_dp = [float("inf")]*n
rev_dp = [float("inf")]*n

as_is_dp[0] = 0
rev_dp[0] = c[0]

for ind in range(1, n):
    if strings[ind - 1] <= strings[ind]:
        as_is_dp[ind] = min(as_is_dp[ind], as_is_dp[ind - 1])    

    if  rev_str[ind - 1] <= strings[ind]:
        as_is_dp[ind] = min(as_is_dp[ind], rev_dp[ind - 1])
    
    if strings[ind - 1] <= rev_str[ind]:
        rev_dp[ind] = min(rev_dp[ind], as_is_dp[ind - 1] + c[ind])
    
    if rev_str[ind - 1] <= rev_str[ind]:
        rev_dp[ind] = min(rev_dp[ind], rev_dp[ind - 1] + c[ind])
    

_min = min(as_is_dp[-1], rev_dp[-1])
if _min == float('inf'):
    print(-1)

else:
    print(_min)

        
