from heapq import heappop, heappush, heapify

t = int(input())

for _ in range(t):
    n, time = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    heap = []


    for ind in range(n):
        ai = a[ind]
        bi = b[ind]

        if ai <= time:
            heappush(heap, (-bi,-ai, ind + 1))

        time -= 1

    if heap:
        print(heap[0][2])
    
    else:
        print(-1)

        