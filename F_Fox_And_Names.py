from collections import deque, defaultdict


def topoSort(n, words):
    graph = defaultdict(list)
    indegree = defaultdict(int)

    for ind in range(1, n):
        
        var_ind = 0
        word1 = words[ind - 1]
        word2 = words[ind]

        while var_ind < len(word1) and var_ind < len(word2) and word1[var_ind] == word2[var_ind]:
            var_ind += 1
        
        if var_ind < len(word1) and var_ind < len(word2):
            graph[word1[var_ind]].append(word2[var_ind])
            indegree[word2[var_ind]] += 1
        
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

        added = set(order)
        ans = []
        
        for _ord in range(ord('a'), ord('z') + 1):
            if chr(_ord) not in added:
                ans.append(chr(_ord))

        return ''.join(order + ans)

    return "Impossible"



n = int(input())
words = []

for _ in range(n):
    words.append(input())

print(topoSort(n, words))