



n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

left = 0
ops = 0
count = 1
val = a[0]

for right in range(1, n):
    ops += (right - left)*(a[right] - a[right - 1])

    while ops > k:
        ops -= a[right] - a[left]
        left += 1
    
    if right - left + 1 > count:
        count = right - left + 1
        val = a[right]

print(count, val)
