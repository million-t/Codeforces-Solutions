n, k = map(int, input().split())
h = list(map(int, input().split()))


min_height_ind = 0
min_sum = float('inf')

win_sum = 0

left = 0

for right, height in enumerate(h):
    win_sum += height
    
    if right - left >= k:
        win_sum -= h[left]
        left += 1
    
    if right - left + 1 == k and win_sum < min_sum:
        min_height_ind = left
        min_sum = win_sum

print(min_height_ind + 1)
