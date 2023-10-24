from collections import defaultdict

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))

    count1 = 0
    first_color_third_pos = -1
    for ind, col in enumerate(c):
        if col == c[0]:
            count1 += 1
            if count1 == k:
                first_color_third_pos = ind
                break
    
    count2 = 0
    last_color_third_pos = -1
    for ind, col in enumerate(c[::-1]):
        if col == c[-1]:
            count2 += 1
            if count2 == k:
                last_color_third_pos = n - ind - 1
                break
    
    if first_color_third_pos == -1 or last_color_third_pos == -1:
        print('NO')
    
    elif c[0] == c[-1] or first_color_third_pos < last_color_third_pos:
        print('YES')
    
    else:
        print('NO')