
a, b = map(int, input().split())
res = []

while b >= a:
    
    res.append(b)
    if not b%2:
        b //= 2

    elif not (b - 1) % 10:
        b = (b - 1)//10
    
    else:
        break
        

    

if res[-1] == a:
    print('YES')
    print(len(res))
    print(*res[::-1])

else:
    print('NO')