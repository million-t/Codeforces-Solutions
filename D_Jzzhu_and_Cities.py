from heapq import heappop, heappush


n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, x = map(int, input().split())

    graph[u].append((v, x, 0))
    graph[v].append((u, x, 0))


heap = [(0, 1, 0)]
trains = []
for _ in range(k):
    s, y = map(int, input().split())
    heappush(heap, (y, s, 1))
    # graph[1].append((s, y, 1))
    # graph[s].append((1, y, 1))
    # trains.append((s, y))



dist = [float('inf')]*(n + 1)
dist[0] = 0
temp = [0]*(n + 1)

while heap:

    w, cur, r = heappop(heap)

    if w >= dist[cur]:
        if r == 0 and w == temp[cur]:
            temp[cur] = 0
        continue
    
    if r == 1:        
        temp[cur] = 1
        

    dist[cur] = w
    for neigh, leng, route in graph[cur]:
        heappush(heap, (w + leng, neigh, route))

print(k - sum(temp))