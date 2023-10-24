from collections import deque


n = int(input())
graph = [set() for _ in range(n + 1)]


for _ in range(n - 1):
    x, y = map(int, input().split())
    graph[x].add(y)
    graph[y].add(x)

a = list(map(int, input().split()))

tree = [set() for _ in range(n + 1)]

visited = set([1])
queue = deque([1])

while queue:
    size = len(queue)
    
    for _ in range(size):
        cur = queue.popleft()
        
        for neigh in graph[cur]:
            if neigh not in visited:
                queue.append(neigh)
                visited.add(neigh)
                tree[cur].add(neigh)
                
                



queue = deque([1])
if a[0] != 1:
    print('No')
    exit()


pos = 1
while queue:
    size = len(queue)
    
    for _ in range(size):
        cur = queue.popleft()
        

        
        for ind in range(pos, pos + len(tree[cur])):
            neigh = a[ind]
            if neigh in tree[cur]:
                queue.append(neigh)
                

            else:
                print('No')
                exit()
             

        pos += len(tree[cur])



print('Yes')