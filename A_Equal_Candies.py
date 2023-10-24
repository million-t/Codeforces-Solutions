


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))


    _min = min(a)
    ans = 0

    for num in a:
        ans += num - _min
    
    print(ans)