
import sys, threading


def dfs(graph, cur, s, ans):
    global count

    w, b = 0, 0
    if s[cur - 1] == 'W':
        w += 1
    
    else:
        b += 1

    for neigh in graph[cur]:
        wc, bc = dfs(graph, neigh, s, ans)
        w += wc
        b += bc
    if w == b:
        ans[cur] = 1

    return w, b







def main():

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        s = input()

        graph = [[] for i in range(n + 1)]

        for ind, par in enumerate(a):
            graph[par].append(ind + 2)
        
        ans = [0]*(n + 1)
        dfs(graph, 1, s, ans)
        print(sum(ans))



sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
