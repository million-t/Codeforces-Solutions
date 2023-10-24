from bisect import bisect_left, bisect_right

def gcd(a, b):

    if not b:
        return a
    
    return gcd(b, a%b)




a, b = map(int, input().split())

n = int(input())
queries = []

for _ in range(n):
    queries.append(list(map(int, input().split())))

divisors = []
_gcd = gcd(a, b)

for num in range(1, int(_gcd**0.5) + 1):
    if num!=_gcd//num and not _gcd%num:
        divisors.append(num)
        divisors.append(_gcd//num)
        
    elif not _gcd%num:
        divisors.append(num)

divisors.sort()
# print(divisors)
for low, high in queries:
    start = bisect_left(divisors, low)
    end = bisect_right(divisors, high)
    
    if start == end:
        print(-1)
    
    else:
        print(divisors[end - 1])
