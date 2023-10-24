from collections import defaultdict

n, m = map(int, input().split())
edges = []

for _ in range(m):
    edges.append(list(map(int, input().split())))



graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)


stack = [1]
color = [-1]*(n + 1)
color[1] = 1
yes = True

while stack:
    cur = stack.pop()

    for neigh in graph[cur]:

        if color[neigh] != -1:
            if color[neigh] == color[cur]:
                yes = False
                break
        
            continue
        
        color[neigh] = 1 - color[cur]
        stack.append(neigh)

    if not yes:
        break

if not yes:
    print('NO')

else:
    ans = []
    for a, b in edges:
        if color[b]:
            ans.append('0')
        
        else:
            ans.append('1')


    print('YES')
    print(''.join(ans))



