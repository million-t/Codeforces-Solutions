from collections import deque
t = int(input())

for _ in range(t):
    n = int(input())

    graph = [[] for i in range(n)]
    
    for i in range(n - 1):
        u, v = map(int, input().split())

        graph[u - 1].append((v - 1, i))
        graph[v - 1].append((u - 1, i))

    no = False
    start = None
    for node in range(n):
        if len(graph[node]) > 2:
            no = True
            break

        elif len(graph[node]) == 1:
            start = node

    if no:
        print(-1)
        continue    
  
    
    visited = [0]*n
    visited[start] = 1
    queue = deque([start])

    primes = [11, 2]
    prime_ind = 0

    ans = [0]*(n-1)
    while queue:
        cur = queue.popleft()

        for neigh, edge in graph[cur]:

            if not visited[neigh]:
                visited[neigh] = 1
                queue.append(neigh)

                ans[edge] = primes[prime_ind]
                prime_ind = 1 - prime_ind
    

    

    print(*ans)
    
