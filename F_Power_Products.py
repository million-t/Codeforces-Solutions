from collections import defaultdict

def factorize(num):
    factors = defaultdict(int)
    factor = 2

    while factor*factor <= num:
        while not num%factor:
            factors[factor] += 1
            num //= factor

        factor += 1

    if num > 1:
        factors[num] += 1

    return factors


n, k = map(int, input().split())
nums = list(map(int, input().split()))


seen = defaultdict(int)
count = 0


for num in nums:
    
    factors = factorize(num)

    b = 1
    a = 1
    for base, _pow in factors.items():
        _pow =  _pow%k
        a *= base**_pow
        
        if _pow:
            b *= base**(k - _pow)

    count += seen[b]
    seen[a] += 1

print(count)



