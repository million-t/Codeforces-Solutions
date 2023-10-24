import math
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    evens = 0

    wrong = 0
    for ind, num in enumerate(a):
        if ind%2 != num%2:
            wrong += 1
        
        if not num%2:
            evens += 1
    
    if not wrong:
        print(0)
    elif wrong and evens != math.ceil(n/2):
        print(-1)
        

    else:
        print(wrong//2)