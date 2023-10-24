from collections import deque


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    
    queue = deque()
    yes = True
    target = sum(a)
    run_sum = 0
    queue.append([0, -1])
    # flag = 0


    for ind, ai in enumerate(a):
        if ai >= target:
            yes = False
        
        run_sum += ai
        while queue and queue[-1][0] >= run_sum:
            queue.pop()
                    
        while queue and run_sum - queue[0][0] >= target:
            prev, start = queue.popleft()
            if not (start == -1 and ind == n - 1):
                yes = False
                
                break 
            # flag = 1

        if not yes:
            break
        
        queue.append([run_sum, ind])
    
    # print(flag)
    if yes:
        print('YES')
    
    else:
        print('NO')
    