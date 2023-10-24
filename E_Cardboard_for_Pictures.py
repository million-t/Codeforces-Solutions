import math

t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    s = list(map(int, input().split()))



    for num in s:
        c -= num*num

    a = 0
    b = 0
    c = -c
    for num in s:
        b += 4*num
        a += 4
    

    temp = math.sqrt((b*b) - (4*a*c))
    print( int((temp - b)/(2*a)) )    
    
    

    
