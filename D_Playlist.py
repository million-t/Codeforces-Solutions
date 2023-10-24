
import sys

inp = list(sys.stdin)
n, k = map(int, inp[0].split())
temp = []

for _ in range(1, n + 1):
    length, beauty = map(int, inp[_].split())
    temp.append((beauty*length, beauty, length))

temp.sort(reverse = True)
res = temp[0][0]
_min = temp[0][1]
_sum = temp[0][2]

for ind in range(1, k):
    prod, b, t = temp[ind]
    _min = min(_min, b)
    _sum += t
    res = max(res, _sum*_min)

print(res)



