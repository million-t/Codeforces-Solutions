


t  = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ones = 0
    non = 0
    


    for num in a:
        if num == 1:
            ones += 1
        
        else:
            non += 1

    
    if 2*ones > (sum(a) - non) or n == 1:
        print('NO')

    else:
        print('YES')
