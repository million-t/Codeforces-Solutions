t = int(input())

for _ in range(t):
    n = int(input())
    
    ans = [float('inf'), float("inf")]
    for i in range(n):
        t, bit_str = input().split()

        prev = None
        for ind, bit in enumerate(bit_str):
            if bit == '1':
                if prev:
                    ans[ind] = 0
                
                ans[ind] = min(ans[ind], int(t))
        
    if float('inf') in ans:
        print(-1)
    
    else:
        print(sum(ans))

