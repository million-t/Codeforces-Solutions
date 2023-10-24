

t = int(input())
for _ in range(t):
    s = input()
    
    res = set()
    ind = 0
    while ind < len(s) -1:

        if s[ind] != s[ind + 1]:
            res.add(s[ind])
            ind += 1
        
        else:
            ind += 2
        
    
    if ind < len(s):
        res.add(s[ind])

    
    print(''.join(sorted(res)))