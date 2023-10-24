from collections import defaultdict

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))


    dp = defaultdict(lambda: defaultdict(int))
    # dp[n - 1].add((a[-1], k))

    for ind in range(n):
        dp[ind][a[ind]] = k

    for ind in range(n - 2, -1, -1):
        for val, _k in dp[ind + 1].items():

            i = 1
            while i <= _k and a[ind] + i <= val + 1 and a[ind] + i:
                dp[ind][a[ind] + i] = max(dp[ind][a[ind] + i], _k - i)
                i += 1 


    _max = max(a)

    for ind, vals in dp.items():
        for (val, k) in vals.items():
            _max = max(_max, val)


    print(_max) 
