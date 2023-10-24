

n, k = map(int, input().split())
ropes = []
for line in range(n):
    ropes.append(int(input()))



def helper(mid, ropes):
    
    pieces = 0
    
    for size in ropes:
        pieces += size//mid
    return pieces


start = 0
end = max(ropes)


while start <= end:

    mid = start + (end - start)/2
    temp = helper(mid, ropes)
    if temp >= k:
        start = mid + 0.0000001
    
    else:
        end = mid - 0.0000001

print(start)
