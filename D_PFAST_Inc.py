from heapq import heapify, heappop, heappush
from collections import defaultdict

n, m = map(int, input().split())
graph = {}

for _ in range(n):
    graph[input()] = []



for _ in range(m):
    a, b = input().split()
    graph[a].append(b)
    graph[b].append(a)


heap = []

for node in graph:
    heappush(heap, (len(graph[node]), node))

color = defaultdict(str)

while heap:
    
    num_neighs, cur = heappop(heap)
    if color[cur]:
        continue
    
    color[cur] = '1'

    for neigh in graph[cur]:
        if color[neigh] == '1':
            color[cur] = '0'
            break

        color[neigh] = '0'
    

ans = []
for name, val in color.items():
    if val == '1':
        ans.append(name)

ans.sort()
print(len(ans))

for name in ans:
    print(name)




