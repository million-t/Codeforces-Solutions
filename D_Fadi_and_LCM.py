x = int(input())


def gcd(a, b):
    if not b:
        return a
    
    return gcd(b, a%b)



a, b = 1, x


for num in range(int(x**0.5), 0, -1):
    if x%num == 0 and num*(x//num)/gcd(num, x//num) == x:
        a = num
        b = x//num
        break
    
print(a, b)
