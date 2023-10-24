


n = int(input())
p = list(map(int, input().split()))


prof = 0     
p += p
for ind in range(1, 2*n):
    if p[ind] - p[ind - 1] > 0:
        prof += p[ind] - p[ind - 1]


print(prof)