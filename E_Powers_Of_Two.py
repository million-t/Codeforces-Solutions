import heapq

n, k = map(int, input().split())

binary = bin(n)

count = binary.count('1')

if k < count:
    print('NO')

else:
    heap = []

    for ind, bit in enumerate(binary[::-1]):
        
        if bit == '1':
            heapq.heappush(heap, -1*(2**ind))
        
    while len(heap) < k:
        if heap[0] > -2:
            break

        top = -1*(heapq.heappop(heap))
        half = top//2
        heapq.heappush(heap, half*-1)
        heapq.heappush(heap, half*-1)
    
    for i in range(len(heap)):
        heap[i] = -1*heap[i]

    if len(heap) == k:
        print('YES')
        print(*heap[::-1])

    else:
        # print(heap)
        print('NO')
