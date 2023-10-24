


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    odds = []
    evens = []
    for ai in a:
        if ai&1:
            odds.append(ai)
        
        else:
            evens.append(ai)

    
    odds.extend(evens)
    print(*odds)