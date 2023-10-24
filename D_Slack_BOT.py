class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.onpath = 0



root = TrieNode()
n = int(input())
words = []

for _ in range(n):
    word = input()
    cur = root
    words.append(word)

    for char in word:
        if char not in cur.children:
            cur.children[char] = TrieNode()

        cur = cur.children[char]
        cur.onpath += 1

    cur.isEnd = True

ans = []

for word in words:
    
    cur = root
    temp = 0
    level = 0

    for char in word:
        cur = cur.children[char]
        level += 1
        if cur.onpath > 1:
            temp = level
    
    ans.append(temp)

for num in ans:
    print(num)

