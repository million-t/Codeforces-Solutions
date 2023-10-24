from collections import deque

xs, ys, xe, ye = map(int, input().split())
n = int(input())

allowed = set()

for _ in range(n):
    r, a, b = map(int, input().split())

    for cell in range(a, b + 1):
        allowed.add((r, cell))
    

visited = set([(xs, ys)])
queue = deque([(xs, ys)])

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
]

moves = 0
yes = False

while queue:
    
    size = len(queue)
    for _ in range(size):
        row, col = queue.popleft()

        if (row, col) == (xe, ye):
            yes = True
            print(moves)
            
            break

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if (nr, nc) in allowed and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))
    
    moves += 1

if not yes:
    print(-1)