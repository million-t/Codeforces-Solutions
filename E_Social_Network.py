from heapq import heappop, heappush, heapify


class DSU:
    def __init__(self, n):
        
        self.rep = {num: num for num in range(1, n + 1)}
        self.rank = [1]*(n + 1)
        self.max_rank = []
    
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
            self.rank[rep_x] += self.rank[rep_y]
            heappush(self.max_rank, (-self.rank[rep_x], rep_x)) 
        
        else:
            self.rep[rep_x] = rep_y
            self.rank[rep_y] += self.rank[rep_x]
            heappush(self.max_rank, (-self.rank[rep_y], rep_y))
    
    def getMaxRank(self):
        return -self.max_rank[0][0]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    
n, d = map(int, input().split())

edges = []
for _ in range(d):
    edges.append(list(map(int, input().split())))

union_find = DSU(n + 1)

# ans = []
for x, y in edges:
    repx = union_find.find(x)
    repy = union_find.find(y)

    if repx == repy:
        rank1, prev_rep1 = heappop(union_find.max_rank)
        rank2, prev_rep2 = heappop(union_find.max_rank)
        rep1 = union_find.find(prev_rep1)
        rep2 = union_find.find(prev_rep2)
        
        print(-rank1 + -rank2 - 1)
        union_find.union(rep1, rep2)

    else:

        union_find.union(x, y)
        print(union_find.getMaxRank() - 1)

