

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    

    difs = []
    expected = sum(range(1, n + 1))
    seen  = set()
    
    if 1 <= a[0] <= n:
        seen.add(a[0])
        expected -= a[0]
    
    else:    
        difs.append(a[0])

    for ind in range(1, n - 1):
        dif = a[ind] - a[ind - 1]
        if dif not in seen and 1 <= dif <= n:
            seen.add(dif)
            expected -= dif

        else:    
            difs.append(dif)



    if len(difs) == 1 and expected == difs[0]:
        print('YES')
    
    elif not difs and sum(seen) + expected == sum(range(1, n + 1)):
        print('YES')
        
    else:
        print('NO')