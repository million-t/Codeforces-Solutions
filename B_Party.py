from collections import defaultdict

def sn(): return int(input())
def ln(): return map(int, input().split())
def lst(): return list(map(int, input().split()))

n = sn()

emp = defaultdict(list)
for _ in range(1, n + 1):
    sup = sn()
    
    emp[sup].append(_)

stack = [-1]

def dfs(node):

    stack = [(node, 1)]
    
    levels = 0
    while stack:
        par, prev_h = stack.pop()
        levels = max(levels, prev_h)
        for em in emp[par]:
            stack.append((em, prev_h + 1))

    return levels

min_group = 0
for child in emp[-1]:
    min_group = max(min_group, dfs(child))

print(min_group)