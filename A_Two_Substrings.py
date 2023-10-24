from heapq import heapify, heappop, heappush

s = input()
ab = []
ba = []

for ind in range(1, len(s)):
    if s[ind - 1] == 'A' and s[ind] == 'B':
        ab.append((ind - 1, ind))
    
    elif s[ind - 1] == 'B' and s[ind] == 'A':
        ba.append((ind - 1, ind))

if ab and ba:
    abFirst = ab[0]
    abLast = ab[-1]
    baFirst = ba[0]
    baLast = ba[-1]

    if abFirst[1] < baLast[0] or baFirst[1] < abLast[0]:
        print('YES')

    else:
        print('NO') 

else:
    print('NO')


