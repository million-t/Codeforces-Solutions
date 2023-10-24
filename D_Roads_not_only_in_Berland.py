from collections import defaultdict

def dfs(graph, u, visited):
    visited[u] = True
    count = 1
    for v in graph[u]:
        if not visited[v]:
            count += dfs(graph, v, visited)
    return count

t = int(input())
n, m = map(int, input().split())
graph = defaultdict(list)
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
bridge = -1
for i in range(1, m+1):
    u, v = map(int, input().split())
    graph[u].remove(v)
    graph[v].remove(u)
    visited = [False] * (n+1)
    unreachable = 0
    for j in range(1, n+1):
        if not visited[j]:
            count = dfs(graph, j, visited)
            unreachable += count * (n - count)
    if unreachable > count:
        count = unreachable
        bridge = i
    graph[u].append(v)
    graph[v].append(u)

print(bridge)