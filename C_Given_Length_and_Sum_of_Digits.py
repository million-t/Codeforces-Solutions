


m, s = map(int, input().split())


if m == 1 and s == 0:
    print(0, 0)
    exit()





arr = [0]*m
add = True
while s  and add:
    add = False
    for ind in range(m):
        if arr[ind] < 9:
            add = True
            temp = arr[ind]
            arr[ind] += min(9 - arr[ind], s)
            s -= min(9 - temp, s)

_min = arr[:]
for i in range(m-1, -1, -1):
    if _min[i] != 0:
        _min[i] -= 1
        _min[-1] += 1
        break

if s > 0 or arr[0] == 0 or _min[-1] == 0:
    print(-1, -1)

else: 
    temp = ''.join(map(str, arr))
    print(''.join(map(str, _min))[::-1], temp)
    
