
t  = int(input())



for _ in range(t):
    n, k = list(map( lambda , input().split()))

    
    bin_k = bin(k)[::-1]

    kth_special = 0
    for index, bit in enumerate(bin_k):
        if bit == '1':
            kth_special += n**index
        
    
    print(kth_special % (10**9 + 7))


