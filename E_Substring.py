from collections import  deque, Counter

n, m = map(int, input().split())
s = input()
graph = [[]for _ in range(n)]
indegree = [0]*n

for _ in range(m):
    x, y = map(int, input().split())
    graph[x - 1].append(y - 1)
    indegree[y - 1] += 1

ord_a = ord("a")
queue = deque()

dp = [[] for _ in range(n)]
for node in range(n):
    if not indegree[node]:
        c = [0]*26
        key = ord(s[node]) - ord_a
        c[key] += 1
        dp[node] = c
        queue.append(node)


count = 0
ans = 1

while queue:

    for _ in range(len(queue)):
        cur = queue.popleft()
        count += 1

        for neigh in graph[cur]:
            indegree[neigh] -= 1

            if not indegree[neigh]:
                new_count = dp[cur].copy()
                key = ord(s[neigh]) - ord_a
                new_count[key] += 1
                ans = max(ans, new_count[key])
                dp[neigh] = new_count
                
                queue.append(neigh)

if count == n:
    print(ans)

else:
    print(-1)




