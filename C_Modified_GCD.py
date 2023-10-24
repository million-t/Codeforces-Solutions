from bisect import bisect_left, bisect_right

def find_factors(a):

    factors = set([1, a])

    for num in range(2, int(a**0.5) + 1):
        if not a%num:
            factors.add(a//num)
            factors.add(num)
    
    return factors


a, b = map(int, input().split())

a_divisors = find_factors(a)
b_divisors = find_factors(b)


common = sorted(a_divisors.intersection(b_divisors))



n = int(input())

for _ in range(n):
    low, high = map(int, input().split())

    left, right = bisect_left(common, low), bisect_right(common, high)
    
    if left < right:
        print(common[right - 1])
    
    else:
        print(-1)


