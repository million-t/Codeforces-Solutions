import math
from heapq import heappush, heappop, heapify

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))


a.sort()
b.sort()


def possible(a, b, n):
    points = 0
    ind = 0
    for i, num in enumerate(a):
        
        while ind < n and b[ind] < num:
            ind += 1
        
        if ind < n and b[ind] >= num:
            points += 1
            ind += 1 

    
    return points

points = possible(a, b, n)

rem = n - points

print(math.ceil(rem/2))


