

n, m = map(int, input().split())
a = list(map(int, input().split()))


left_over = sum(a) - m

if left_over < 0:
    print(-1)
    exit()

if left_over == 0:
    print(n)
    exit()


temp = sorted(a, reverse=True)
ans = 0
run = 0
ind = 0
while ind < n:
    
    if run < m:
        ans += 1

    run += temp[ind]
    subt = 1
    while left_over > 0 and ind < n - 1 and temp[ind + 1] > subt and subt <= left_over:
        left_over -= subt
        run += temp[ind + 1] - subt
        subt += 1
        ind += 1
    
    
    
    ind += 1

print(ans)
    
    
    


