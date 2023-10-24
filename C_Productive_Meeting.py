import heapq
t = int(input())

for _ in range(t):
    n = int(input())
    people = list(map(int, input().split()))


    heap = []

    for ind, talks in enumerate(people):
        if talks:
            heapq.heappush(heap, (-1*talks, ind + 1))

    ans = 0
    pairs = []

    while len(heap) > 1:
        best1, ind1 = heapq.heappop(heap)
        best2, ind2 = heapq.heappop(heap)

        best1 += 1
        best2 += 1
        
        if best1 < 0:
            heapq.heappush(heap, (best1, ind1))
        
        if best2 < 0:
            heapq.heappush(heap, (best2, ind2))
        
        pairs.append((min(ind1, ind2), max(ind1, ind2)))
        ans += 1
    

    print(ans)
    for x, y in pairs:
        print(x, y)

