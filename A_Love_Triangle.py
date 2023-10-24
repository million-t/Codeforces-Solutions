n = int(input())

planes = list(map(int, input().split()))


yes = False
for ind in range(n):
    _next = planes[ind] - 1
    visits = set()
    
    j = 4
    while j:
        visits.add(_next + 1)
        _next = planes[_next] - 1
        
        j-= 1
    if _next + 1 == planes[ind] and len(visits) == 3:
        
        yes = True
        break

if yes:
    print('YES')

else:
    print('NO')



