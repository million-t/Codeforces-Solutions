

class DSU:
    def __init__(self, obj):
        
        self.rep = {num: num for num in obj}
        self.rank = {num: 1 for num in obj}
    
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



ans = 0
n, m = map(int, input().split())

temp = []
components = set()


for ith in range(n):
    lang = list(map(int, input().split()))
    
    if len(lang) == 1:
        ans += 1

    for ind in range(1, len(lang)):
        components.add(lang[ind])

        if ind > 1:
            temp.append((lang[ind], lang[ind - 1]))

    
        
    
union_find = DSU(components)

for x, y in temp:
    union_find.union(x, y)


components = list(components)
for ind in range(len(components)):
    first_lang = components[ind]

    for j in range(ind + 1, len(components)):
        sec_lang = components[j]

        if not union_find.is_connected(first_lang, sec_lang):
            union_find.union(first_lang, sec_lang)
            ans += 1

print(ans)





