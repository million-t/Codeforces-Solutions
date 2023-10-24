n, k, d = map(int, input().split())


max_count = k - d + 1
memo = {}
def dp(path_weight, edge, count, max_count, n, k):
    
    if edge in memo:
        return memo[edge]

    if count > max_count or path_weight > n:
        return 0
    
    if path_weight == n:
        return 1

    ans = 0
    for num in range(1, k + 1):
        ans += dp(path_weight + num, num, count + 1, max_count, n, k)
    
    memo[edge] = ans
    return ans

ans = 0
for _ in range(d, k + 1):
    ans += dp(0, _, 1, max_count, n, k)
    
print(ans)