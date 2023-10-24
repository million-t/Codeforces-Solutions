from collections import defaultdict, deque


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

color = [0]*(n + 1)
visited = set()
def bfs(node):

    visited.add(node)
    queue = deque([node])
    color[node] = 1
    steps = 0
    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            for neigh in graph[cur]:
                if neigh in visited:
                    if color[neigh] == color[cur]:
                        return False
                    
                    continue

                color[neigh] = 3 - color[cur]
                queue.append(neigh)
                visited.add(neigh)
        
        steps += 1
        
    if steps == 1:
        color[node] = 0
        
    return True

ans = {2: [], 1:[]}
for node in range(1, n + 1):
    if node not in visited:
        res = bfs(node)
        if not res:
            print(-1)
            exit()
for node, col in enumerate(color):
    if col != 0:
        ans[col].append(node)

print(len(ans[1]))
print(*ans[1])
print(len(ans[2]))
print(*ans[2])




