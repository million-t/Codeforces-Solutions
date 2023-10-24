


n, m = map(int, input().split())

graph = {}

for node in range(1, n + 1):
    graph[node] = []

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, -c))
    edges.append((a, b, c))

dist = [float('inf')]*(n + 1)
dist[1] = 1

for _ in range(n - 1):

    for node in graph:
        for neigh, weight in graph[node]:
            if dist[node] != float('inf') and dist[node] + weight < dist[neigh]:
                dist[neigh] = dist[node] + weight
        

ans = []
for node in graph:
    for neigh, weight in graph[node]:
        if dist[node] != float('inf') and dist[node] + weight < dist[neigh]:
            dist[neigh] = dist[node] + weight
            ans.append(node)
            ans.append(neigh)

if ans:
    print("YES")
    print(*ans)

else:
    print('NO')