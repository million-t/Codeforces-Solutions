



n, l , r = map(int, input().split())
memo = {}
h = {}

def dp(cur):
    if cur < 2:
        memo[cur] = int(cur == 0)
        h[cur] = 0
        return cur
    
    half = cur//2
    mod = cur%2

    temp = dp(half)
    
    memo[temp + 1] = memo[temp] + int(mod == 0)
    memo[temp*2 + 1] = memo[temp]*2 + int(mod == 0)
    
    h[half + 1] = memo[temp + 1]
    h[cur] = memo[temp*2 + 1]


    return temp*2 + 1



def helper(cur, left):
    if cur < 2:
        return h[cur]
    
    half = cur//2
    mod = cur%2
    if left < half:
        return helper(half, left)

    elif left == half:
        return h[half]
    
    elif left == half + 1:
        return h[half + 1]
    
    else:
        return h[half + 1] + helper(half, left - half)
    






dp(n)
_max = max(memo)
print(memo)
# print(r - l + 1 - (memo[_max] - helper(n, min(l, _max - l)) - helper(n, min(r - 1, _max - r - 1))))








    

    