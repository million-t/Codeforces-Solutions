from collections import defaultdict

n, m = map(int, input().split())
cats = list(map(int, input().split()))

graph = defaultdict(list)
for _ in range(n - 1):

    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

stack = [(1, cats[0])]
visited = [0]*(n + 1)
visited[1] = 1
count = 0


while stack:
    cur, prev = stack.pop()
    
    is_leaf = 1
    for child in graph[cur]:
        
        if visited[child]:
            continue
        is_leaf = 0
        visited[child] = 1

        if cats[child - 1]:
            if prev + 1 > m:
                continue

            else:
                stack.append((child, prev + 1))
        
        else:
            stack.append((child, 0))

    if is_leaf:
        count += 1

        
print(count)