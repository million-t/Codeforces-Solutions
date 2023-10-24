


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()


    no = False
    for ind in range(1, n):
        if a[ind] > a[ind - 1] + 1:
            no = True
            break
    
    if no:
        print('NO')
    
    else:
        print('YES')
