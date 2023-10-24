t= int(input())
for _ in range(t):
    s = int(input())
    ans = []
    n = 9
    while s > n:
        s -= n
        ans.append(str(n))
        n -= 1
    
    if s:
        ans.append(str(s))
    
    print(''.join(sorted(ans)))