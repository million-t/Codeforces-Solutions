from collections import defaultdict, deque

n, m, k = map(int, input().split())
graph = [[]for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


banned = set()
for _ in range(k):
    banned.add(tuple(map(int, input().split())))



visited = set([()])
queue = deque([(1, [1])])
parent = {n:-1}
yes = False
roads = 0

while queue:

    for _ in range(len(queue)):
        cur, past = queue.popleft()
        if cur == n:
           yes = True
           break
        

        for neigh in graph[cur]:
            copy = past[-2:]
            copy.append(neigh)
            
            if neigh != 1 and (cur, neigh) not in visited and tuple(copy) not in banned:
                queue.append((neigh, copy))
                visited.add((cur, neigh))
                parent[neigh] = cur 
                print(cur, neigh)
    roads += 1
    if yes:
        break
if not yes:
    print(-1)

else:

    temp = [n]
    
    while parent[temp[-1]] != -1:
        temp.append(parent[temp[-1]])

    print(len(temp) - 1)    

    print(*temp[::-1])
