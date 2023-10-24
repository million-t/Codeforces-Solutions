class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    root = TrieNode()

    for num in a:

        cur = root
        for ind in range(31, -1, -1):
            bit = 1&(num >> ind) 
            if bit not in cur.children:
                cur.children[bit] = TrieNode()
            
            cur = cur.children[bit]
    
    ans = 0
    for num in a:
        
        cur = root
        temp = 0

        for ind in range(31, -1, -1):
            bit = 1&(num >> ind) 

            val = 0
            if bit == 1:
                if 0 in cur.children:
                    cur = cur.children[0]
                    val = 0
                
                elif 1 in cur.children:
                    cur = cur.children[1]
                    val = 1
            
            else:
                if 1 in cur.children:
                    cur = cur.children[1]
                    val = 1
                
                elif 0 in cur.children:
                    cur = cur.children[0]
                    val = 0
            
            temp <<= 1
            temp ^= val
        
        ans = max(ans, num^temp)

    print(ans)
        







