t = int(input())
for _ in range(t):
    n, m, k = list(map(int, input().split()))
    a = ''.join(sorted(input()))
    b = ''.join(sorted(input()))
    
    p1 = p2 = 0

    c = []
    a_cnt = 0
    b_cnt = 0
    while p1 < n and p2 < m:
        if a_cnt < k and b_cnt < k and a[p1:] <= b[p2:]:
            c.append(a[p1])
            p1 += 1
            a_cnt += 1
        elif a_cnt < k and b_cnt < k and a[p1:] >= b[p2:]:
            c.append(b[p2])
            p2 += 1
            b_cnt += 1
        
        elif a_cnt < k:
            c.append(a[p1])
            p1 += 1
            a_cnt += 1
            b_cnt = 0
        else:
            c.append(b[p2])
            p2 += 1
            a_cnt = 0
            b_cnt += 1


    
    print(''.join(c))

