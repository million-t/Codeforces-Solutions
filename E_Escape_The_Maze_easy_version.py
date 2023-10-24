import sys, threading



def dfs(tree, visited, cur, moves, friend):

    if friend[cur]:
        return 1, 'NO'
    
    closest_friend = float('inf')
    yes = 'YES'
    for neigh in tree[cur]:
        if neigh not in visited:
            visited.add(neigh)
            dist, is_possible = dfs(tree, visited, neigh, moves + 1, friend)
            closest_friend = min(closest_friend, dist)
    
    # if closest_friend > moves
    




def main():

    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        x = list(map(int, input().split()))

        tree = [[] for node in range(n + 1)]
        for line in range(n - 1):
            u, v = map(int, input().split())
            tree[u].append(v)
            tree[v].append(u)


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()






    

