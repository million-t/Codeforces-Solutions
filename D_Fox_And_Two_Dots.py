from collections import deque

n , m = map(int, input().split())

board = []
for _ in range(n):
    board.append(input())



directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def inbound(row, col):
    return 0 <= row < len(board) and 0 <= col < len(board[0])


visited = set()
def bfs(r, c):
    

    queue = deque([(r, c, (-1, -1))])
    visited.add((r, c))
    

    while queue:

        row, col, par = queue.popleft()

        for dr, dc in directions:
            nr, nc = row + dr , col + dc
            if not inbound(nr, nc) or board[row][col] != board[nr][nc]:
                continue
            
            if (nr, nc) in visited and (nr, nc) != par:
                return True

            elif (nr, nc) not in visited:
            
                queue.append((nr, nc, (row, col)))
                visited.add((nr, nc))
            
            
    
    return False
    


yes = False
for row in range(n):
    for col in range(m):
        if (row, col) not in visited:
            
            if bfs(row, col):
                yes = True
                break

if yes:
    print('Yes')

else:
    print('No')



