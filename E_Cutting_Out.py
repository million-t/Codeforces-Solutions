from collections import Counter
from heapq import heappop, heappush
n, k = map(int, input().split())
s = list(map(int, input().split()))


freq = Counter(s)

heap = []
least = n
for num, count in freq.items():
    least = min(least, count)
    heappush(heap, (count//k, count%k, num))


while len(heap) < k:
    count1, mod, num1 = heappop(heap)
    count1 = - count1
    heappush(heap, (-(count1//2),mod, num))
    heappush(heap, ((count1//2) - count1,mod, num))


ans 
print(*heap)




