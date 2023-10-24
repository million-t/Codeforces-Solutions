
class DSU:
    def __init__(self, obj):

        self.rep = {n: n for n in obj}
        self.rank = {n : 1 for n in obj}
        self.size = {n: 1 for n in obj}


    def find(self, x):

        root = x
        while root != self.rep[root]:
            root = self.rep[root]
        
        while root != x:
            temp = self.rep[x]
            self.rep[x] = root
            x = temp
        
        return root
    
    def union(self, x, y):
        repx = self.find(x)
        repy = self.find(y)
        if repx == repy:
            return

        if self.rank[repx] > self.rank[repy]:
            self.size[repx] += self.size[repy]

            self.rep[repy] = repx
        
        elif self.rank[repx] > self.rank[repy]:
            self.size[repy] += self.size[repx]

            self.rep[repx] = repy


        else:
            self.size[repy] += self.size[repx]

            self.rep[repx] = repy

            self.rank[repy] += 1
    
    def sizee(self, x):
        return self.size[self.find(x)]


n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(input())


directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
def inbound(r, c, n, m):
    return 0 <= r < n and 0 <= c < m

temp = []

for row in range(n):
    for col in range(m):
        temp.append((row, col))

uf = DSU(temp)

for row in range(n):
    for col in range(m):
        if mat[row][col] == '.':
            if row - 1 >= 0 and mat[row - 1][col] == '.':
                uf.union((row, col), (row - 1, col))
            
            if col - 1 >= 0 and mat[row][col - 1] == '.':
                uf.union((row, col), (row, col - 1))
            
            # if (row, col) == (0, m - 2):
            #     # print(tmp)
            #     print(uf.sizee((row, col)))
    

ans = []



for row in range(n):
    rr = []
    for col in range(m):

        if mat[row][col] == '*':
            tmp = set()


            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                # if (nr, nc) == (0, 1):
                #     print('y')
                #     print(mat[nr][nc])
                if inbound(nr, nc, n , m) and mat[nr][nc] == '.':
                    # print('r')
                    tmp.add(uf.find((nr, nc)))
            
            
            con = 1
            for key in tmp:
                con += uf.sizee(key)
            
            rr.append(str(con%10))
        
        else:
            rr.append('.')


    ans.append(rr)


res = []

for row in ans:
    res.append(''.join(row))

for row in res:
    print(row)
            




    

