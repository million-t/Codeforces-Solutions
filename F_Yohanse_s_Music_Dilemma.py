




n, m = map(int, input().split())

grid = [[0]*102 for _ in range(102)]

for _ in range(n):
    x, y = map(int, input().split())
    grid[x + 1][y + 1] += 1

q = []
for _ in range(m):
    q.append(tuple(map(int, input().split())))



for row in range(1, 102):
    for col in range(1, 102):
        grid[row][col] += grid[row - 1][col] + grid[row][col - 1] - grid[row - 1][col - 1]


for sx, sy, ex, ey in q:
    ex += 1
    ey += 1
    sx += 1
    sy += 1

    ans = grid[ex][ey] + grid[sx - 1][sy - 1] - grid[ex][sy - 1] - grid[sx - 1][ey]
    print(ans)
