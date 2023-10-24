from collections import deque
n, m, p = map(int, input().split())

grid = []
pm = []
for _ in range(n):
    grid.append(input())

pm = list(map(int, input().split()))


directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]


pos = {
    0: (0, 0),
    1: (-1, 0),
    2: (1, 0),
    3: (0, -1),
    4: (0, 1)
}

def inbound(row, col, n, m):
    return 0 <= row < n and 0 <= col < m

cur = (0, 0)
for row in range(n):
    for col in range(m):
        if grid[row][col] == 'M':
            cur = (row, col)
            break


start = cur
for i in pm:
    dr, dc = pos[i]
    start = start[0] + dr, start[1] + dc

queue = deque([start])
visited = set()
for posit in queue:
    visited.add(posit)

steps = 1
count = 1
while queue:

    if count > p:
        break

    size = len(queue)
    count += 1
    inc = 0
    for _ in range(size):
        row, col = queue.popleft()
        

        
        
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if inbound(nr, nc, n, m) and (nr, nc) not in visited and grid[nr][nc] != '#':
                queue.append((nr, nc))
                visited.add((nr, nc))
                inc += 1
    steps += inc

    
    

print(steps)


