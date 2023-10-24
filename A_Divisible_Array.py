t = int(input())

for _ in range(t):
    n = int(input())

    ans = []

    for num in range(1, n + 1):
        ans.append(num*2)
    
    print(*ans)