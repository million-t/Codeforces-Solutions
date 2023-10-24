t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    b = sorted(a)

    yes = True
    for ai, bi in zip(a, b):
        if ai%2 != bi%2:
            yes = False
            break
    
    if yes:
        print('YES')
    
    else:
        print('NO')