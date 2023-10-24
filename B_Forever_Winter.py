from collections import defaultdict, deque
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())

    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))

    graph = defaultdict(list)
    indegree = defaultdict(int)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        indegree[u] += 1
        indegree[v] += 1
    

    queue = deque([])

    for node in graph:
        if indegree[node] == 1:
            queue.append(node)
    
    
    ans = []
    while queue:
        size = len(queue)
        ans.append(len(queue))
        
        for j in range(size):
            cur = queue.popleft()

            for neigh in graph[cur]:
                indegree[neigh] -= 1
                if indegree[neigh] == 1:
                    queue.append(neigh)

    # print(ans)
    print(ans[1], ans[0]//ans[1])