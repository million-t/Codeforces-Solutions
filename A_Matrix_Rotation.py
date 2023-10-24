n = int(input())
for _ in range(n):
    mat = []
    mat.append(list(map(int, input().split())))
    mat.append(list(map(int, input().split())))

    def rotate(mat):
        ans = []
        for col in range(2):
            newRow = []
            for row in range(1, -1, -1):
                newRow.append(mat[row][col])
            ans.append(newRow)
        return ans
    def checkBeautiful(mat):
        return mat[0][0] < mat[0][1] and mat[0][0] < mat[1][0] and \
        mat[0][1] < mat[1][1] and mat[1][0] < mat[1][1]
    beauty = False
    for _ in range(4):
        if checkBeautiful(mat):
            print('YES')
            beauty = True
            break 
        mat = rotate(mat)
    if not beauty:
        print('NO')

