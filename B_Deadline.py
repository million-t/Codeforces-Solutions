from math import ceil

t = int(input())
for _ in range(t):
    n, d = map(int, input().split())

    yes = False
    for num in range(n):
        days = num + ceil(d/(num + 1))
        
        if days <= n:
            yes = True
            break

    if yes:
        print('YES')
    
    else:
        print('NO')