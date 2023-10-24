from collections import defaultdict

n = int(input())

v = input()
t = input()

graph = defaultdict(list)

for ind in range(n):
    graph[v[ind]].append(t[ind])
    graph[t[ind]].append(v[ind])

ans = []
visited = set()
def dfs(node):

    visited.add(node)
    stack = [node]

    while stack:
        cur = stack.pop()

        for neigh in graph[cur]:
            if neigh not in visited:
                visited.add(neigh)
                ans.append([cur, neigh])
                stack.append(neigh)


for node in graph:
    if node not in visited:
        dfs(node)
    

print(len(ans))
for line in ans:
    print(*line)
    
