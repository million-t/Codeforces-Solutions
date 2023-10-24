from collections import Counter

t = int(input())
for _ in range(t):
    n , k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0

    for ind in range(n):
        a[ind] = a[ind]%k

    count = Counter(a)
    # x = 0
    
    for mod, freq in count.items():
        
        if mod:
            ans = max(ans, (freq - 1)*k + k - mod + 1)
            

    print(ans) 
