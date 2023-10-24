import heapq


n = int(input())
potions = list(map(int, input().split()))

heap = [0]
_sum = 0
count = 0

for potion in potions:
    
    least_neg = heap[0]
    if least_neg > potion and _sum + potion < 0:
        continue
    
    if potion >= 0:
        _sum += potion
    
    elif _sum + potion >= 0:
        _sum += potion
        heapq.heappush(heap, potion)
    
    else:
        _sum += potion - heapq.heappop(heap)
        heapq.heappush(heap, potion)
        count -= 1
    
    count += 1


print(count)

