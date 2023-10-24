import heapq

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    minHeap = []

    for num in a:
        heapq.heappush(minHeap, num)
    

    
    for _ in range(m):
        least = heapq.heappop(minHeap)
        heapq.heappush(minHeap, b[_])
    
    print(sum(minHeap))