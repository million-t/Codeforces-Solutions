t = int(input())

def findFactor(n):
    
    fact = 0
    while not n % 2:
        n //= 2
        fact += 1
    
    return fact, n

for _ in range(t):
    n = int(input())

    nums = list(map(int, input().split()))
    temp = []

    power = 0
    for num in nums:
        factor, new_val = findFactor(num)
        power += factor

        temp.append(new_val)
    
    max_odd = max(temp)

    _max = max_odd*(2**power) + sum(temp) - max_odd
    print(_max)
