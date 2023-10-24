import heapq

n = int(input())

ops = []
for _ in range(n):
    ops.append(input())

heap = []

printable = []

for op in ops:
    if op.startswith('insert'):
        val = int(op.split()[1])
        heapq.heappush(heap, val)
        printable.append(op)
    
    elif op.startswith('getMin'):
        
        val = int(op.split()[1])
        if heap:
            cur_least = heap[0]
            
            if val < cur_least:
                heapq.heappush(heap, val)
                printable.append(f'insert {val}')
                printable.append(op)

            elif val > cur_least:
                
                while heap and heap[0] < val:
                    heapq.heappop(heap)
                    printable.append(f'removeMin')

                if not heap or heap[0] > val:
                    heapq.heappush(heap, val)
                    printable.append(f'insert {val}')
                    printable.append(op)
                
                else:
                
                    printable.append(op)
            
            else:
                printable.append(op)
        else:
            heapq.heappush(heap, val)
            printable.append(f'insert {val}')
            printable.append(op)

    elif op.startswith("removeMin"):
        if heap:
            heapq.heappop(heap)
            
        else:
            printable.append('insert 0')
        printable.append(op)

print(len(printable))

for line in printable:
    print(line)