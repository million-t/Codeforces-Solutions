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
        
        if self.rank[rep_x] > self.rank[rep_y]:
            self.rep[rep_y] = rep_x
        
        elif self.rank[rep_x] < self.rank[rep_y]:
            self.rep[rep_x] = rep_y
        
        else:
            self.rep[rep_y] = rep_x
            self.rank[rep_x] += 1
        
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


inp = list(sys.stdin)
t = int(inp[0])
i = 1

for line in range(t):
    
    n = int(inp[i])

    a = list(map(int, inp[i + 1].split()))
    b = list(map(int, inp[i + 2].split()))
    d = list(map(int, inp[i + 3].split()))
    i += 4     


    
    union_find = DSU(n)
    ind = 0 

    for x, y in zip(a, b):
        union_find.union(x, y)
        if x == y:
            d[ind] = x
        
        ind += 1
    
    excluded = set()
    for ind in range(n):
        if d[ind]:
            excluded.add(union_find.find(d[ind]))
        
    
    valid_reps = set()
    
    for x in a:
        rep = union_find.find(x)
        if rep not in excluded:
            valid_reps.add(rep)

    print((2**len(valid_reps))%1_000_000_007)
