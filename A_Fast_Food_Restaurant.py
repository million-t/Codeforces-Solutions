



t = int(input())

for _ in range(t):

    a, b, c = sorted(map(int, input().split()), reverse=True)
    
    ans = 0
    stack = []
    if a:
        ans += 1
        a -= 1
    if b:
        ans += 1
        b -= 1
    if c:
        ans += 1
        c -= 1
    
    if a and b:
        ans += 1
        a -= 1
        b -= 1
    
    if b  and c:
        b -= 1
        c -= 1
        ans += 1

    
    if a and c:
        a -= 1
        c -= 1
        ans += 1

    
    if a and b and c:
        a -= 1
        b -= 1
        c -= 1
        ans += 1
    
    print(ans)
    
    
    


    