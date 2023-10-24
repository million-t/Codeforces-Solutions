from collections import defaultdict, deque
# import sys, threading

# def dfs(node, tree, path, ans):
    
#     path.append(node)
#     if not tree[node]:
        
#         ans.append(path)
    
#     else:
        
#         dfs(tree[node][0], tree, path, ans)

#         for child in range(1, len(tree[node])):
#             dfs(tree[node][child], tree, [], ans)

# def main():

t = int( input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    root = 1
    
    indegree = defaultdict(int)

    for ind, num in enumerate(p):
        if ind + 1 != num:
            indegree[num] += 1
        
        else:
            root = num
    
    
    queue = deque([])

    for node in range(1, n + 1):
        if not indegree[node]:
            
            queue.append([node, [node]])

    paths = []

    seen = set()
    while queue:
        cur, path = queue.popleft()
        
        parent = p[cur - 1]
        indegree[parent] -= 1
        if not indegree[parent]:
            path.append(parent)
            queue.append([parent, path])
            
        
        else:
            paths.append(path)
    
    print(len(paths))
    for path in paths:
        print(len(path))
        print(*path[::-1])
    
    print()


        # ans = []
        # dfs(root, tree, [], ans)
        
        # print(len(ans))

        # for path in ans:
            
        #     print(len(path))
        #     print(*path)
        
        # print()




# sys.setrecursionlimit(1 << 30)
# threading.stack_size(1 << 27)

# main_thread = threading.Thread(target=main)
# main_thread.start()
# main_thread.join()