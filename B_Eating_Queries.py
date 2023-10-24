from bisect import bisect_left

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    queries = []
    for qi in range(q):
        queries.append(int(input()))


    a.sort(reverse=True)

    prefix = [a[0]]
    for i in range(1, n):
        prefix.append(prefix[-1] + a[i])
    
    res = []

    for qi in queries:
        ans = bisect_left(prefix, qi) + 1
        if ans > n:
            ans = -1
        res.append(ans)
    
    for line in res:
        print(line)
