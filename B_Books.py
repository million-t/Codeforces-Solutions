


n, t = map(int, input().split())
a = list(map(int, input().split()))


# pref = [0]
# for ai in a:
#     pref.append(pref[-1] + ai)


left = 0
run = 0
max_num = 0
for right in range(n):
    run += a[right]

    while run > t and left <= right:
        run -= a[left]
        left += 1
    
    max_num = max(max_num, right - left + 1)

print(max_num)
