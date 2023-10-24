t = int(input())
for _ in range(t):
    inp = list(map(int, input().split()))
    inp.sort()

    if inp[-1] + inp[-2] >= 10:
        print('YES')
    
    else:
        print('NO')