t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    fav = list(map(int, input().split()))

    _sum = x*(x + 1)//2

    for num in fav:
        if num <= x:
            _sum -= num + num
    
    print(_sum)
