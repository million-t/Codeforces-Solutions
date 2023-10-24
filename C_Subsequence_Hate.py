t = int(input())

for _ in range(t):
    s = input()

    pref = [0]
    suf  = [0]
    for ind in range(len(s)):
        pref.append(pref[-1] + int(s[ind]))
    
    for bit in s[::-1]:
        suf.append(suf[-1] + int(bit))
    suf.pop()
    pref.pop()
    suf.reverse()
    
    min_op = float('inf')
    length = len(s)
    for ind in range(len(s)):
        inc = pref[ind] + (length - ind -1) - suf[ind]
        dec = ind - pref[ind] + suf[ind]
        min_op = min(min_op, inc, dec)
        
    
    print(min_op)