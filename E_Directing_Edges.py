from collections import deque, defaultdict

    

def topoSort(n, graph, indegree, undirected):

    

    queue = deque()

    for node in range(n):
        if not indegree[node]:
            queue.append(node)


    topo_order = []

    while queue:
        cur = queue.popleft()
        topo_order.append(cur)

        for neigh in graph[cur]:
            indegree[neigh] -= 1

            if not indegree[neigh]:
                queue.append(neigh)
    

    res = []
    if len(topo_order) == n:

        temp = {node: ind for ind, node in enumerate(topo_order)}
        for x, y in undirected:
            x, y = x - 1, y - 1
            
            if temp[x] > temp[y]:
                res.append([y + 1, x + 1])
            
            else:
                res.append([x + 1, y + 1])
        
        return 'YES', res

    return 'NO', res




t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    directed = []
    undirected = []
    
    for i in range(m):
        direct, x, y = map(int, input().split())
        if direct:
            directed.append((x, y))
        
        else:
            undirected.append((x, y))
    
    graph = [[] for _2 in range(n)]
    indegree = defaultdict(int)

    for x, y in directed:
        graph[x - 1].append(y - 1)
        indegree[y-1] += 1
    

    yes, res = topoSort(n, graph, indegree, undirected)

    if yes == 'NO':
        print(yes)
    
    else:
        res.extend(directed)

        print(yes)
        for each in res:
            print(*each)