n = int(input())
arr = list(map(int, input().split()))

arr.sort()
left = 0
mx = 0
for right in range(n):
    while left <= right and arr[right] - arr[left] > 5:
        left += 1

    mx = max(mx, right - left + 1)

print(mx)
       