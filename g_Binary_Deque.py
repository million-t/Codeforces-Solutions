from collections import defaultdict
tests = int(input())

for _ in range(tests):
    
    n, s = map(int, input().split())
    stream = list(map(int, input().split()))

    prefix = [0]
    for bit in stream:
        prefix.append(prefix[-1] + bit)
    
    # if s == prefix[-1]:
    #     print(0)
    
    
    if s <= prefix[-1]:
        
    
        seen = defaultdict(int)
        max_win = 0

        for ind, p in enumerate(prefix):

            dif = p - s
            
            if dif in seen:
                max_win = max(max_win, ind - seen[dif])
                
            if p not in seen:
                seen[p] = ind
            
            
        print(n - max_win)
    
    else:
        print(-1)
    
    