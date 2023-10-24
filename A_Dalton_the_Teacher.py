from math import ceil

t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))


    unhap = 0
    for ind, num in enumerate(p):
        if ind + 1 == num:
            unhap += 1
    
    print(ceil(unhap/2))
