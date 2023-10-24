t = int(input())

for _ in range(t):
    n = int(input())
    temp = []
    for i in range(n):
        a, b = map(int, input().split())
        temp.append((a, b, i))
    
    temp.sort()

    ans = 0
    res = 0
    for a, b, i in temp:
        if a <= 10 and b > ans:
            res = i
            ans = b

    
    print(res + 1)