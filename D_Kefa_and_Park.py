from collections import defaultdict
def sn(): return int(input())
def ln(): return map(int, input().split())
def lst(): return list(map(int, input().split()))


n, m = ln()
cats = lst()

graph = defaultdict(list)

for _ in range(n - 1):
    x, y = ln()
    if x < y:

        graph[x].append(y)
    else:
        graph[y].append(x)

st = 1 if cats[0] else 0
stack = [(1, st)]

count = 0
while stack:
    cur, prev = stack.pop()
    
    if not graph[cur]:
        count += 1

    for child in graph[cur]:
        if cats[child - 1]:
            if prev + 1 > m:
                continue

            else:
                stack.append((child, prev + 1))
        
        else:
            stack.append((child, 0))

# print(graph)   

print(count)