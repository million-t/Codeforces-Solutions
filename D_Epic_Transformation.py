import heapq
from collections import Counter

def solve(n, nums):

    counts = Counter(nums)
    heap = []

    for num, count in counts.items():
        heapq.heappush(heap, (-1*count, num))

    while len(heap) > 1:
        count1, top1 = heapq.heappop(heap)
        count2, top2 = heapq.heappop(heap)

        count1 += 1
        if count1:
            heapq.heappush(heap, (count1, top1))

        count2 += 1
        if count2:
            heapq.heappush(heap, (count2, top2))

    ans = 0
    for count, num in heap:
        ans += -1*count

    return ans



t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    print(solve(n, nums))
