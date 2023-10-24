

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    


    target = -1
    for ind in range(n - 2, -1, -1):
        if a[ind] > a[ind + 1]:
            target = ind
            break

    
    _max = 0
    for num in range(target + 1):
        _max = max(_max, a[num])

    print(_max)