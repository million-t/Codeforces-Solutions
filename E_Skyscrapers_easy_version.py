

n = int(input())
m = list(map(int, input().split()))



for ind, pivot in enumerate(m):
    
    temp = 0
    for dec_ind in range(ind, -1, -1):
        val = m[dec_ind]
        
# aobut the quic brown fox