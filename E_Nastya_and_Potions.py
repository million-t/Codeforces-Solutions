from collections import defaultdict, deque
import sys

inp = list(sys.stdin)
t = int(inp[0])
i = 1
for _ in range(t):
    n, k = map(int, inp[i].split())
    c = list(map(int, inp[i + 1].split()))
    p = set(map(int, inp[i + 2].split()))


    i += 3
    graph = [[] for j in range(n + 1)]
    indegree = defaultdict(int)
    alt = [0]*(n + 1)
    s = 1
    for j in range(i, n + i):
        prevs = list(map(int, inp[j].split()))

        for ind in range(1, prevs[0] + 1):
            e= prevs[ind]
            graph[e].append(s)
            indegree[s] += 1
        s += 1

    i += n

    queue = deque()
    for node in range(1, n + 1):
        if node in p:
            queue.append((node, 0))
            
        elif not indegree[node]:
            queue.append((node, c[node - 1]))

    ans = [0]*n
    while queue:
        for p in range(len(queue)):
            cur, cost = queue.popleft()

            ans[cur - 1] = cost 
            for neigh in graph[cur]:
                indegree[neigh] -= 1
                alt[neigh - 1] += cost
                if not indegree[neigh]:
                    queue.append((neigh, min(c[neigh - 1], alt[neigh - 1])))

    print(*ans)
    
    