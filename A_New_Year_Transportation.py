n, t = map(int, input().split())
a = list(map(int, input().split()))

cell = 1
yes = False
while cell < n:
    if cell == t:
        yes = True
        break

    cell = cell + a[cell - 1]

if yes or cell == t:
    print('YES')

else:
    print('NO')
