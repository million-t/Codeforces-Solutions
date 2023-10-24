n, k = map(int, input().split())

edges = []
for _ in range(n - 1):
    edges.append(list(map(int, input().split())))


graph = [[]for _ in range(n + 1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)
    


visited = set()


