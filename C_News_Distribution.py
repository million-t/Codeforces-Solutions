from collections import defaultdict
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
n, m = map(int, inp[0].split())

line = 1


union_find = DSU(n + 1)

for _ in range(m):
    group = list(map(int, inp[line].split()))
    line += 1

    k = group[0]

    for ind in range(1, len(group)):
        p1 = group[ind]
        for j in range(ind, len(group)):
            union_find.union(p1, group[j])
            
        break

ans = []
rep_mem = defaultdict(list)
num_rep = {}
for num in range(1, n + 1):
    rep = union_find.find(num)
    num_rep[num] = rep
    rep_mem[rep].append(num)


ans = []
for num in num_rep:
    rep = num_rep[num]
    ans.append(len(rep_mem[rep]))

print(*ans)
