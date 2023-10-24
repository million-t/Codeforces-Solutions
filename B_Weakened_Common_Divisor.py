


def prime_bases(num):
    factors = set()
    factor = 2

    while factor*factor <= num:
        while not num%factor:
            factors.add(factor)
            num //= factor

        factor += 1

    if num > 1:
        factors.add(num)

    return factors



n = int(input())
pair_product = []

for _ in range(n):
    a, b = map(int, input().split())
    pair_product.append((a, b))


ans = -1
possible_factors = prime_bases(pair_product[0][0]).union(prime_bases(pair_product[0][1]))


for prime in possible_factors:

    count = 1
    for ind in range(1, n):
    
        if pair_product[ind][0]%prime == 0 or pair_product[ind][1]%prime == 0:
            count += 1
    
    if count == n:
        ans = prime
        break

print(ans)


