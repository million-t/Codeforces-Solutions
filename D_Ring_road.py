from collections import defaultdict
n = int(input())

graph = defaultdict(list)





total = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    total += c
    graph[a].append((b, 0))
    graph[b].append((a, c))



    

stack = [(1, 0)]
visited = [0]*(n + 1)
parent = {}
res = 0
fin = 0
fin_set = False

while stack:
    
    cur, cost = stack.pop()

    if visited[cur]:
        if cur == 1 and parent[parent[cur]] != 1 and not fin_set:
            fin_set = True
            fin = cost
            
        continue


    res += cost
    visited[cur] = 1


    
    
    for neigh in graph[cur]:
        parent[neigh[0]] = cur
        stack.append(neigh)
        

res += fin

print(min(res, total - res))






