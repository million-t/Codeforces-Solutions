from collections import defaultdict


n = int(input())
inc = defaultdict(list)
out = defaultdict(list)

graph = []

for cur in range(n):
    s = list(map(int, input().split()))
    graph.append(s)

remove = list(map(int, input().split()))


dist = [[float('inf')] * n for _ in range(n)]
ans = []
for i in range(n + 1):
    f[i] = False

for x in range(1, n + 1):
    ans[x] = 0
    k = del_list[x]
    f[k] = True
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            data[i][j] = min(data[i][j], data[i][k] + data[k][j])
            if f[i] and f[j]:
                ans[x] += data[i][j]

for i in range(n, 0, -1):
    print(ans[i], end=" ")