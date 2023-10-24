n = int(input())
arr = list(map(int, input().split()))

mx = 0
i = 0
while i < n:
    length = 0
    while i < n - 1 and arr[i] <= arr[i+1]:
        length += 1
        i += 1
    mx = max(length + 1, mx)
    i += 1
print(mx)
    