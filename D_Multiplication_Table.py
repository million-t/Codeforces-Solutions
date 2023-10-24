


def check(lim, mid):
    ans = 0

    for row in range(1, lim + 1):
        ans += min((mid - 1)//row, n)
    
    return ans





n, m, k = map(int, input().split())
start = 1
end = n*m


while start <= end:
    mid = start + (end - start)//2

    lim = min(mid, m)
    if check(lim, mid) < k:
        start = mid + 1
    
    else:
        end = mid - 1

print(start - 1)

