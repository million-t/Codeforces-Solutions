

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    ans = 0
    left = 0
    for right in range(1, n):
        dif = a[right] - a[right - 1]
        if dif > k:
            left = right

        ans = max(ans, right - left)
    print(n - ans - 1)
