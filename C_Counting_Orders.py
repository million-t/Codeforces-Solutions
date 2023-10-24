t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    product = 1

    cur = 0
    yes = True

    for ind, num in enumerate(a):

        
        while cur < n and b[cur] < num:
            cur += 1
        
        smaller_nums = cur
        if smaller_nums - ind < 1:
            yes = False
            break

        product = (product*((smaller_nums - ind)%1_000_000_007))%1_000_000_007
    

    if not yes:
        print(0)
    
    else:
        print(product)

