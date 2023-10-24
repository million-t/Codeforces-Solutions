from collections import Counter

class TrieNode:
    def __init__(self):
        self.children = [None]*2
        self.isEnd = 0


q = int(input())
root = TrieNode()
cur = root

for ind in range(31, -1, -1):
    bit = 0 
    if not cur.children[bit]:
        cur.children[bit] = TrieNode()
    
    cur = cur.children[bit]
    cur.isEnd += 1

for _ in range(q):
    sign, x = input().split()
    num = int(x)

    
    if sign == '+':
        cur = root
        for ind in range(31, -1, -1):
            bit = 1&(num >> ind) 
            if not cur.children[bit]:
                cur.children[bit] = TrieNode()
            
            cur = cur.children[bit]
            cur.isEnd += 1

    elif sign == '-':
        cur = root
        

        for ind in range(31, -1, -1):
            bit = 1&(num >> ind)
            par = cur
            cur = cur.children[bit]
            cur.isEnd -= 1
            if not cur.isEnd:
                par.children[bit] = None

    else:
        ans = 0
            
        cur = root
        temp = 0

        for ind in range(31, -1, -1):
            bit = 1&(num >> ind) 
            comp = 1 - bit
            val = 0
            if cur.children[comp]:
                cur = cur.children[comp]
                val = comp
            
            elif cur.children[bit]:
                cur = cur.children[bit]
                val = bit
        
            temp <<= 1
            temp ^= val
        
        
        print(num^temp)

        




