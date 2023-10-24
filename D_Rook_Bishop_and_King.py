


r1, c1, r2, c2 = map(int, input().split())

r1 -= 1
r2 -= 1
c1 -= 1
c2 -= 1
rook = 0

if ( not (r1 == r2 and c1 == c2)) and (r1 == r2 or c1 ==c2):
    rook = 1

elif not (r1 == r2 and c1 == c2):
    rook = 2

bishop = 0

def isodd(num):
    return num&1
if isodd(r1) == isodd(c1):
    if isodd(r2) == isodd(c2):
        if (not (r1 == r2 and c1 == c2)) and c1 != c2 and abs(r2 - r1)/abs(c2 - c1) == 1:
            bishop = 1
        
        elif not (r1 == r2 and c1 == c2):
            bishop = 2
    
else:
    if isodd(r2) != isodd(c2):
        if (not (r1 == r2 and c1 == c2)) and c1 != c2 and abs(r2 - r1)/abs(c2 - c1) == 1:
            bishop = 1
        
        elif not (r1 == r2 and c1 == c2):
            bishop = 2

king = max(abs(r1 - r2), abs(c1 - c2))

print(rook, bishop, king)

