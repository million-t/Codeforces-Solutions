

t = int(input())

for _ in range(t):
    
    input()
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    t = list(map(int, input().split()))


    ans = [float('inf')]*(n)
    for p, t in zip(a, t):
        ans[p - 1] = t
    


    for ind in range(1, n):
    
        ans[ind] = min(ans[ind- 1] + 1, ans[ind])
        ans[~ind] = min(ans[~(ind- 1)] + 1, ans[~ind])


    print(*ans)