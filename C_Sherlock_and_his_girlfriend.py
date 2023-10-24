n = int(input())

def findPrimes(n):
    is_prime = [1]*(n)
    is_prime[0] = is_prime[1] = 0

    for num in range(2, n):
        if not is_prime[num]:
            continue

        j = num*2
        while j < n:    
            is_prime[j] = 0
            
            j += num
    
    return is_prime

colors = findPrimes(n + 2)[2:]

for i in range(len(colors)):
    colors[i] = 1 if colors[i] else 2

if n < 3:
    print(1)

else:
    print(2)

print(*colors)


