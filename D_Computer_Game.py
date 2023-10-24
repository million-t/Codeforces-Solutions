
directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, -1),
    (-1, 1),
    (1, 1),
    (-1, -1)
]

def inbound(row, col, n):
    return 0 <= row < 2 and 0 <= col < n

def dfs(graph, n):

    stack = [(0, 0)]
    visited = set([(0, 0)])
    while stack:
        row, col = stack.pop()

        if (row, col) == (1, n - 1):
            return 'YES'
        
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if inbound(nr, nc, n) and (nr, nc) not in visited and graph[nr][nc] == '0':
                stack.append((nr,nc))
                visited.add((nr, nc))
    
    return 'NO'


t = int(input())



for _ in range(t):
    n = int(input())
    row1 = input()
    row2 = input()
    graph = [row1, row2]

    print(dfs(graph, n))



