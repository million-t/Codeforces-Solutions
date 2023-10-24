from heapq import heappush, heappop

t = int(input())

for _ in range(t):
    n = int(input())

    heap = []
    for num in range(1, n + 1):
        heappush(heap, -1*num)


    output = []
    for _ in range(n - 1):
        large1 = heappop(heap)*-1
        large2 = heappop(heap)*-1
        output.append((large1, large2))

        new = (large1 + large2 + 1)//2
        heappush(heap, -1*new)

        
    
    print(heap[0]*-1)
    for num1, num2 in output:
        print(num1, num2)
        
