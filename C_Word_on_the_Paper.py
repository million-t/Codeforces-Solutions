t = int(input())
for _ in range(t):

    grid = []
    for i in range(8):
        grid.append(input())

    target = [0, 0]
    br = False
    for row in range(8):
        for col in range(8):
            if grid[row][col] != '.':
                target = [row, col]
                br = True
                break
        if br:
            break
    
    ans = []
    col = target[1]
    for row in range(target[0], 8):
        if grid[row][col] == '.':
            break

        ans.append(grid[row][col])
    
    print(''.join(ans))