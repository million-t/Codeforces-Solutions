from collections import defaultdict
from heapq import heappush, heappop

import sys, threading

def main():
        


    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    indegree = defaultdict(int)

    for _ in range(m):
        v, u = map(int, input().split())
        graph[v].append(u)
        indegree[u] += 1

    greed = [node for node in range(n)]
    visited = set()

    def dfs(node):
        if node in visited:
            return greed[node - 1]

        visited.add(node)
        temp = node
        
        for neigh in graph[node]:
            temp = min(dfs(neigh), temp)
        
        greed[node - 1] = temp
        return temp



    for node in range(1, n + 1):
        if node not in visited:
            dfs(node)

    heap = []
    for node in range(1, n + 1):
        if not indegree[node]:
            heappush(heap, (greed[node - 1], node))

    ans = [0]*n
    # perm_vals = sorted([str(val) for val in range(1, n + 1)])
    perm_ind = 1
    # print(greed)

    while heap:

        importance, cur = heappop(heap)
        ans[cur - 1] = perm_ind
        perm_ind += 1 

        for neigh in graph[cur]:
            indegree[neigh] -= 1
            
            if not indegree[neigh]:
                heappush(heap, (greed[neigh - 1], neigh))

    print(*ans)


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
