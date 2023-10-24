t = int(input())

for _ in range(t):

    n = int(input())
    s = list(map(int, input().split()))
    f = list(map(int, input().split()))


    dur = [f[0] - s[0]]

    for ind in range(1, n):
        dur.append(f[ind] - max(s[ind], f[ind - 1]))
    
    print(*dur)