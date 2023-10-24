from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    _min = min(a)

    b, c = [], []

    for num in a:
        if num == _min:
            b.append(num)
        
        else:
            c.append(num)
    
    if not b or not c:
        print(-1)
    
    else:
        print(len(b), len(c))
        print(*b)
        print(*c)