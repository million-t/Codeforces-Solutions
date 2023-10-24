
class DSU:
    def __init__(self, n):
        
        self.rep = {num: num for num in range(1, n + 1)}
        self.rank = [1]*(n + 1)
    
    def find(self, x):
        
        root = x
        while root != self.rep[root]:
            root = self.rep[root]
        
        while x != root:
            temp = self.rep[x]
            self.rep[x] = root
            x = temp
        
        return root
    
    def union(self, x, y):
        rep_x = self.find(x)
        rep_y = self.find(y)
        
        if rep_x == rep_y:
            return
        
        if self.rank[rep_x] > self.rank[rep_y]:
            self.rep[rep_y] = rep_x
        
        elif self.rank[rep_x] < self.rank[rep_y]:
            self.rep[rep_x] = rep_y
        
        else:
            self.rep[rep_y] = rep_x
            self.rank[rep_x] += 1
        
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

n, m1, m2 = list(map(int, input().split()))


mocha = DSU(n)
for _ in range(m1):
    x, y = map(int, input().split())
    mocha.union(x, y)


diana = DSU(n)
for _ in range(m2):
    x, y = map(int, input().split())
    diana.union(x, y)


ans = []
for u in range(1, n + 1):
    for v in range(u + 1, n + 1):
        if (not mocha.is_connected(u, v)) and (not diana.is_connected(u, v)):
            mocha.union(u, v)
            diana.union(u, v) 
            ans.append([u, v])


print(len(ans))
for pair in ans:
    print(*pair)
