

t = int(input())
for _ in range(t):
    b, c, h = map(int, input().split())

    temp = c + h
    ans = 1
    b -= 1
    while b and temp:
        b -= 1
        temp -= 1
        ans += 2
          
    print(ans)