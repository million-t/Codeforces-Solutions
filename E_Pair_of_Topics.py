n = int(input())
teacher = list(map(int, input().split()))
student = list(map(int, input().split()))

for i in range(n):
    teacher[i] -= student[i]

left, right = 0, n - 1
prev = 0
while left < n:
    
    while right >= left and teacher[left] + teacher[right] > 0:
        right -= 1

    prev += n - right - 2
    left += 1
    if right < left: right = left
print(prev)