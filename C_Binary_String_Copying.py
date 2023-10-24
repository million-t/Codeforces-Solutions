

t = int(input())

for _ in range(t):
    n, m  = map(int, input().split())
    s = input()

    pairs = []
    for line in range(m):
        pairs.append(map(int, input().split()))
    
    pref = []
    for bit in s:
        if pref:
            pref.append((1 - int(bit)) + pref[-1])

        else:
            pref.append((1 - int(bit)))
    
    seen = set()
    
    for l, r in pairs:
        right, left = pref[r - 1], pref[l - 1]
        mid = l + right - left - int(s[l - 1])
        seen.add((right - left, mid))  

    print(len(seen))




