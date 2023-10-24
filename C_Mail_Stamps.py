from collections import defaultdict
n = int(input())

graph = defaultdict(list)
for _ in range(n):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

start = None

for node in graph:
    if len(graph[node]) == 1 and not start:
        start = node
        break
    
stack = [start]
visited = set([start])
ans = []

while stack:
    cur = stack.pop()
    ans.append(cur)

    for neigh in graph[cur]:
        if neigh not in visited:
            visited.add(neigh)
            stack.append(neigh)

print(*ans)
