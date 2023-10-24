from collections import defaultdict
n = int(input())

root = 'polycarp'
graph = defaultdict(list)
for _ in range(n):
    
    n1, rep, n2 = input().split()
    graph[n2.lower()].append(n1.lower())
    





stack = [(root , 1)]
visited = set()
visited.add(root)
max_len = 0

while stack:
    cur, _len = stack.pop()

    max_len = max(max_len, _len)

    for neigh in graph[cur]:
        if neigh not in visited:
            stack.append((neigh, _len + 1))
            visited.add(neigh)

print(max_len)
