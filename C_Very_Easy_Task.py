


n, x, y = map(int, input().split())

if x > y:
    x, y = y, x


def helper(mid, x, y):
    by_x = mid//x
    by_y = mid//y
    return by_x + by_y 

start = 0
end = n

while start  <= end:
    mid = start + (end - start)//2

    if helper(mid, x, y) <= n:
        start = mid + 1
    
    else:
        end = mid - 1

print(start)
