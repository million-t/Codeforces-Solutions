

t = int(input())
for _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))

    pref = {}

    run = 0
    pref[0] = 0
    for ind, num in enumerate(w):
        run += num
        pref[run] = ind + 1
    
    ans = 0 
    run = 0
    for ind, num in enumerate(w[::-1]):
        run += num
        if run in pref and pref[run] + ind + 1 <= n:
            ans = max(ans, pref[run] + ind + 1)
    
    print(ans)