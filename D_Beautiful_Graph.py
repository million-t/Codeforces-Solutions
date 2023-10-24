import sys
MOD = 998244353



def dfs(graph, n):
    
    color = [-1]*(n)

    ans = 1
    for node in range(n):

        if color[node] != -1:
            continue

        
        sub_ans = [0, 1]
        color[node] = 1
         
        stack = [node]
        while stack:
            cur = stack.pop()

            for neigh in graph[cur]:
                if color[neigh] != -1:
                    if color[neigh] == color[cur]:
                        return 0

                    continue

                color[neigh] = 1 - color[cur]
                sub_ans[color[neigh]] += 1

                stack.append(neigh)
        
        ans = (ans*((pow(2, sub_ans[0], MOD) + pow(2, sub_ans[1], MOD))))%MOD

    return ans




inp = list(sys.stdin)
t = int(inp[0])
i = 1

while i < len(inp):
    n, m = map(int, inp[i].split())
    
    graph = [[] for _ in range(n)]
    i += 1
    lim = i + m
    while i < lim and i < len(inp):

        u, v = map(int, inp[i].split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
        i += 1
    
    
    print(dfs(graph, n))

