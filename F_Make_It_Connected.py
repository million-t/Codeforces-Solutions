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
    

n, m = map(int, input().split())

a  = list(map(int, input().split()))
offers = []
for _ in range(m):
    offers.append(list(map(int, input().split())))

union_find = DSU(n + 1)
cost = 0
s_min = min(a)
for x, y, w in offers:
    if max(a[x - 1], a[y - 1]) + s_min > w:
        union_find.union(x, y)
        cost += w
        # seen.add(max(x, y))
        # seen.add(y)

num_rep = {}
for num in range(1, n + 1):
    rep = union_find.find(num)
    num_rep[num] = rep

rep_cost = {}

for num in range(n, 0, -1):
    rep = union_find.find(num)

    if rep in rep_cost: 
        rep_cost[rep] = min(rep_cost[rep], a[num - 1])
    else:
        rep_cost[rep] = a[num - 1]

# ans = 
for rep, _min in rep_cost.items():
    # if _min != s_min:
    cost += s_min + _min

cost -= s_min + 1
    

print(cost)