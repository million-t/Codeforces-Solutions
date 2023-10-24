import heapq

n = int(input())
m = int(input())

heap = []
_max = 0

for _ in range(n):
    people = int(input())
    _max = max(_max, people)
    heapq.heappush(heap, people)

_max += m

while m:
    sparse = heapq.heappop(heap)
    heapq.heappush(heap, sparse + 1)
    m -= 1

print(max(heap), _max)