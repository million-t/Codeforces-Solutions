from collections import defaultdict, deque

indegree = defaultdict(int)
graph = defaultdict(list)
for _ in range(3):
    comp = input()
    if comp[1] == "<":
        graph[comp[0]].append(comp[2])
        indegree[comp[2]] += 1
    
    else:
        graph[comp[2]].append(comp[0])
        indegree[comp[0]] += 1

queue = deque()
for coin in graph:
    if not indegree[coin]:
        queue.append(coin)


topo_order = []
while queue:
    cur = queue.popleft()
    topo_order.append(cur)
    for neigh in graph[cur]:
        indegree[neigh] -= 1
        if not indegree[neigh]:
            queue.append(neigh)

if len(topo_order) == 3:
    print("".join(topo_order))

else:
    print("Impossible")