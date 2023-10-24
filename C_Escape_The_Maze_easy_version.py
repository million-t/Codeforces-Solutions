

import sys, threading

def dfs(tree, visited, cur, held, temp):

    ans = float('inf')
    
    if cur in held:
        ans = 0

    
    for neigh in tree[cur]:
        if neigh not in visited:
            visited.add(neigh)
            ans = min(ans, dfs(tree, visited, neigh, held, temp) + 1)

    
    temp[cur] = ans
    return ans

def helper(tree, vis, cur, moves, temp):
    
    ans = True if len(tree[cur]) == 1 and cur != 1 else False
    for neigh in tree[cur]:
        if neigh not in vis and moves + 1 < temp[neigh]:
            vis.add(neigh)
            ans = ans or helper(tree, vis, neigh, moves + 1, temp)

    return ans




def main():
    t = int(input())
    for _ in range(t):
        input()
        n, k = map(int, input().split())
        
        held = set(map(int, input().split()))
        # line += 1

        tree = [[] for j in range(n  + 1)]
        for i in range( n - 1):
            u, v = map(int, input().split())
            # line += 1
            tree[u].append(v)
            tree[v].append(u)
        
        temp = [n + n]*(n + 1)

        dfs(tree, set([1]), 1, held, temp)
        print('YES' if helper(tree, set([1]), 1, 0, temp) else 'NO')
        






sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
