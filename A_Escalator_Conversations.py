from collections import Counter
t = int(input())

for _ in range(t):
    n, m, k, h = map(int, input().split())
    heights = Counter(map(int, input().split()))

    convos = 0
    for num in range(1, m):
        convos += heights[h - k*num] + heights[k*num + h]
        
    print(convos)