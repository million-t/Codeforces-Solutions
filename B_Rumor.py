n, m = map(int, input().split())

c = list(map(int, input().split()))

edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))


graph = [[] for _ in range(n)]

for a, b in edges:
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


visited = set()
cost = 0

for node in range(n):
    if node in visited:
        continue

    stack = [node]
    visited.add(node)
    cur_cost = c[node]
    while stack:
        cur = stack.pop()

        cur_cost = min(cur_cost, c[cur])
        for neigh in graph[cur]:
            if neigh not in visited:
                stack.append(neigh)
                visited.add(neigh)

    cost += cur_cost

print(cost)
