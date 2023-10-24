import heapq
n = int(input())

heap = []
for _ in range(n):
    l, r = map(int, input().split())
    heapq.heappush(heap, (r, l))

prev = 0
count = 0

while heap:
    right, left = heapq.heappop(heap)
    
    if left > prev:
        prev = right
        count += 1
    

print(count)