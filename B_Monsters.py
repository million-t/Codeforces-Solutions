
import sys

inp = list(sys.stdin)
t = int(inp[0])
i = 1
for _ in range(t):
    n, k = map(int, inp[i].split())
    a = list(map(int, inp[i + 1].split()))

    i += 2
    ter = []
    for ind, num in enumerate(a):
        if num > k:
            temp = num%k
            if not temp:
                temp = k
            ter.append((-(temp), ind))
        else:
            ter.append((-(num), ind))

    ans = []
    ter.sort()
    for cur, ind in ter:
        ans.append(ind + 1)
    
    print(*ans)


