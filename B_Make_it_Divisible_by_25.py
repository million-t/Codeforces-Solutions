t = int(input())

for _ in range(t):
    n = input()

    digs = [dig for dig in n]

    x = len(digs)
    zero = 0
    for ind in range(x - 1, 0, -1):
        if int(digs[ind]) == 0:
            zero = ind
            break
    
    ans = float('inf')
    if zero:
        first = x - zero - 1
        fiveZero = -1
        for ind in range(zero - 1, -1, -1):
            if int(digs[ind]) == 5:
                fiveZero = ind
                break
            elif int(digs[ind]) == 0 and ind > 0:
                fiveZero = ind
                break
        
        if fiveZero != -1:
            ans = first + zero - fiveZero - 1
    
    five = 0
    for ind in range(x - 1, 0, -1):
        if int(digs[ind]) == 5:
            five = ind
            break
    
    if five:
        first = x - five - 1
        twoSeven = -1
        for ind in range(five - 1, -1, -1):
            if int(digs[ind]) == 2 or int(digs[ind]) == 7:
                twoSeven = ind
                break
        
        if twoSeven != -1:
            ans = min(ans, first + five - twoSeven -1 )
    
    print(ans)



    
                


    
    
