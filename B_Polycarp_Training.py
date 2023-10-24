import heapq


n = int(input())
problems = list(map(int, input().split()))


heapq.heapify(problems)

k = 1
while problems:
    top = heapq.heappop(problems)

    if top >= k:
        k += 1
        

    

print(k - 1)


