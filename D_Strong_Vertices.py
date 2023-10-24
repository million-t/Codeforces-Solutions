


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    temp = []
    i = 0
    for ai, bi in zip(a, b):
        temp.append((ai - bi, i))
        i += 1
    temp.sort(reverse = True)
    prev = temp[0][0]
    ans = [temp[0][1] + 1]
    for ind in range(1, n):
        dif, i = temp[ind]
        if dif != prev:
            break
            
        ans.append(i + 1)

    print(len(ans))
    print(*sorted(ans))
