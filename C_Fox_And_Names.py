from collections import deque, defaultdict


def topoSort(n, words):
    graph = defaultdict(list)
    indegree = defaultdict(int)

    for ind in range(1, n):
        
        i = 0
        word1 = words[ind - 1]
        word2 = words[ind]
        while i < len(word1) and i < len(word2) and word1[i] == word2[i]:
            i += 1
        
        if i < len(word1) and i < len(word2):
            graph[word1[i]].append(word2[i])
            indegree[word2[i]] += 1
        
        elif len(word1) > len(word2):
            return 'Impossible'

    queue = deque()

    for node in graph:
        if not indegree[node]:
            queue.append(node)

    order = []
    while queue:
        cur = queue.popleft()
        
        order.append(cur)
        
        for neigh in graph[cur]:
            indegree[neigh] -= 1
            
            if not indegree[neigh]:
                queue.append(neigh)


    if len(order) == len(graph):
        temp = set(order)
        ans = []
        for _ord in range(ord('a'), ord('z') + 1):
            if chr(_ord) not in temp:
                ans.append(chr(_ord))

        return ''.join(order + ans)

    return "Impossible"



n = int(input())
words = []

for _ in range(n):
    words.append(input())

print(topoSort(n, words))