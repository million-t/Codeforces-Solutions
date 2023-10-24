from heapq import heappop, heappush
class DSU:
    def __init__(self, objs):
        
        self.rep = {obj: obj for obj in objs}
        self.rank = {obj: 1 for obj in objs}
    
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
   



t = int(input())

for _ in range(t):
    n = int(input())
    letters = input()


    alpha = [ chr(_ord) for _ord in range(ord('a'), ord('z') + 1)]
    


    res = []
    seen = {}
    uf = DSU(alpha)
    
    for ind, char in enumerate(letters):
        if char not in seen:

            prev = alpha[0]
            for c in alpha:
                if not uf.is_connected(prev, char):
                    break

                prev = c

            uf.union(char, prev)
            seen[char] = prev
            
        res.append(seen[char])

    print(''.join(res)) 
