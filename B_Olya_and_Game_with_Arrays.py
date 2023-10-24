

t = int(input())
for _ in range(t):

    n = int(input())

    
    secs = []
    _min = float('inf')

    for line in range(n):
        m = int(input())
        arr = list(map(int, input().split()))
        
        arr.sort()
        cur_min = arr[0]
        cur_sec_min = arr[1]
        _min = min(_min, cur_min)
        secs.append(cur_sec_min)
    
    secs.sort()
    print(sum(secs) - secs[0] + _min)
