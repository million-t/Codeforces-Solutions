
import sys

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
        
        if self.rank[rep_x] >= self.rank[rep_y]:
            self.rep[rep_y] = rep_x
            self.rank[rep_x] += self.rank[rep_y] 
        else:
            self.rep[rep_x] = rep_y
            self.rank[rep_y] += self.rank[rep_x]
    
    def get_rank(self, x):
        return self.rank[self.find(x)]
        
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)




inp = list(sys.stdin)

n, m = map(int, inp[0].split())

line = 1
edges = []
for _ in range(1, n):
    u, v, w = map(int, inp[_].split())
    edges.append([w, u, v])

q = list(map(int, inp[n].split()))



for ind in range(m):
    q[ind] = (q[ind], ind)


edges.sort()
q.sort()

union_find = DSU(n)
ans = [0]*m
edge_ind = 0
paths = 0

for _max, ind in q:

    while edge_ind < n - 1 and edges[edge_ind][0] <= _max:
        w, u, v = edges[edge_ind]
        comp1 = union_find.get_rank(u)
        comp2 = union_find.get_rank(v)

        union_find.union(u, v)
        paths += comp1*comp2

        edge_ind += 1
    
    ans[ind] = paths

print(*ans)