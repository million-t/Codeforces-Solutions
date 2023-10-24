import heapq 

n = int(input())
w = list(map(int, input().split()))

passengers = input()

min_heap = []
max_heap = []

for ind, width in enumerate(w):
    heapq.heappush(min_heap, (width, ind))


res = []

for passenger in passengers:
    if passenger == '0':
        width, ind = heapq.heappop(min_heap)

        res.append(ind + 1)
        heapq.heappush(max_heap, (width*-1, ind))
    
    else:
        width, ind = heapq.heappop(max_heap)
        res.append(ind + 1)
    

print(*res)