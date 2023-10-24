from collections import Counter
def primes_less_than(n):
    if n < 2: return []
    
    is_prime = [1]*n
    is_prime[0] = is_prime[1] = 0
    
    num = 2
    bound = n**(1/2)
    
    while num <= bound:
        
        if is_prime[num]:
            
            sieve = num*num
            
            while sieve < n:
                is_prime[sieve] = 0
                sieve += num
            
        num += 1
    
    return [index for index, prime in enumerate(is_prime) if prime]
    
n = int(input())
nums = list(map(int, input().split()))

primes = primes_less_than(2*n + 1)[::-1]
count = Counter(nums)
ans  = []
_sum = 0
while len(ans) < n:
    if primes and primes[-1] == _sum + 1 and count[1]:
        ans.append(1)
        primes.pop()
        _sum += 1
        count[1] -= 1
    
    elif primes and primes[-1] == _sum + 2 and count[2]:
        ans.append(2)
        primes.pop()
        _sum += 2
        count[2] -= 1
    elif count[2]:
        ans.append(2)
        _sum += 2
        count[2] -= 1
    elif count[1]:
        ans.append(1)
        _sum += 1
        count[1] -= 1

print(*ans)
