n = int(input())

def is_almost_prime(num):
    factors = set()
    
    factor = 2
    while factor*factor <= num:

        while not num%factor:

            factors.add(factor)
            if len(factors) > 2:
                return False
            
            num //= factor
        
        factor += 1
    
    if num > 1:
        factors.add(num)
    
    return len(factors) == 2



almost_prime = 0
for num in range(1, n + 1):
    
    almost_prime += is_almost_prime(num)


print(almost_prime)